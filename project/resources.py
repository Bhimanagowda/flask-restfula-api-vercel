# API2/project/resources.py

from flask_restful import Resource, reqparse, abort, fields, marshal_with
from project import api, db
from project.models import ToDoModel

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("name", type=str, help="Name is required", required=True)
task_post_args.add_argument("city", type=str, help="City is required", required=True)
task_post_args.add_argument("college", type=str, help="College is required", required=True)
task_post_args.add_argument("passyear", type=int, help="Passyear is required", required=True)

task_update_args = reqparse.RequestParser()
task_update_args.add_argument("name", type=str)
task_update_args.add_argument("city", type=str)
task_update_args.add_argument("college", type=str)
task_update_args.add_argument("passyear", type=int)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'city': fields.String,
    'college': fields.String,
    'passyear': fields.Integer
}

class ToDoList(Resource):
    def get(self):
        todos = ToDoModel.query.all()
        result = []
        for todo in todos:
            result.append({'id': todo.id, 'name': todo.name, 'city': todo.city, 'college': todo.college, 'passyear': todo.passyear})
        return result

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        todo = ToDoModel.query.filter_by(id=id).first()
        if not todo:
            abort(404, message="Todo not found")
        return todo

    @marshal_with(resource_fields)
    def post(self, id):
        args = task_post_args.parse_args()
        todo = ToDoModel.query.filter_by(id=id).first()
        if todo:
            abort(409, message="Todo id already taken")
            
        if (not args['name'] or not args['name'][0].isalpha() or not args['college'] or not args['college'][0].isalpha() or not args['city'] or not args['city'][0].isalpha()):
          abort(400, message="All fields (name, college, and city) must start with an alphabet letter")

        new_todo = ToDoModel(id=id, name=args['name'], city=args['city'], college=args['college'], passyear=args['passyear'])
        db.session.add(new_todo)
        db.session.commit()
        return new_todo, 201

    @marshal_with(resource_fields)
    def put(self, id):
        args = task_update_args.parse_args()
        todo = ToDoModel.query.filter_by(id=id).first()
        if not todo:
            abort(404, message="Todo not found, cannot update")

        if args['name']:
            todo.name = args['name']
        if args['city']:
            todo.city = args['city']
        if args['college']:
            todo.college = args['college']
        if args['passyear']:
            todo.passyear = args['passyear']
        db.session.commit()
        return todo

    def delete(self, id):
        todo = ToDoModel.query.filter_by(id=id).first()
        if not todo:
            abort(404, message="Todo not found")
        db.session.delete(todo)
        db.session.commit()
        return '', 204

api.add_resource(Todo, '/todos/<int:id>')
api.add_resource(ToDoList, '/todos')

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

class HelloName(Resource):
    def get(self, name):
        return {'message': f'Hello, {name}'}

api.add_resource(HelloWorld, "/user")
api.add_resource(HelloName, '/user/<string:name>')
