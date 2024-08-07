//add.html
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById('add-todo-form');

  form.addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent default form submission

    try {
      // Fetch the current list of todos to find the maximum ID
      const response = await fetch('/todos');
      const todos = await response.json();
      
      // Find the maximum ID
      let maxId = 0;
      todos.forEach(todo => {
        if (todo.id > maxId) {
          maxId = todo.id;
        }
      });

      // Calculate the next ID
      const nextId = maxId + 1;

      // Get form data
      const formData = new FormData(form);
      const data = {
        id: nextId, // Assign the next ID
        name: formData.get('name'),
        city: formData.get('city'),
        college: formData.get('college'),
        passyear: parseInt(formData.get('passyear'))
      };

      // Send POST request to the server
      const postResponse = await fetch(`/todos/${nextId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });

      if (postResponse.ok) {
        alert('Successfully added');
        form.reset(); // Reset the form fields
      } else if (postResponse.status === 409) {
        alert('ToDo ID is already taken');
      } else {
        alert('Error adding ToDo');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Error adding ToDo');
    }
  });
});

//update.html
document.addEventListener("DOMContentLoaded", function () {
  const updateForm = document.getElementById('update-todo-form');

  updateForm.addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent default form submission

    // Collect form data
    const id = document.getElementById('id').value;
    const name = document.getElementById('name').value;
    const city = document.getElementById('city').value;
    const college = document.getElementById('college').value;
    const passyear = document.getElementById('passyear').value;

    // Prepare data for PUT request
    const data = {
      name: name,
      city: city,
      college: college,
      passyear: passyear
    };

    try {
      // Send PUT request to update the ToDo item
      const response = await fetch(`/todos/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });

      if (response.ok) {
        alert('ToDo updated successfully');
        updateForm.reset(); // Reset the form fields
      } else if (response.status === 404) {
        alert('ToDo not found');
      } else {
        alert('Error updating ToDo');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Error updating ToDo');
    }
  });
});


//delete.html
document.addEventListener("DOMContentLoaded", function () {
  const deleteForm = document.querySelector('form');

  deleteForm.addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent default form submission

    // Collect form data
    const id = document.getElementById('id').value;

    try {
      // Send DELETE request to remove the ToDo item
      const response = await fetch(`/todos/${id}`, {
        method: 'DELETE',
      });

      if (response.ok) {
        alert('ToDo deleted successfully');
        deleteForm.reset(); // Reset the form fields
      } else if (response.status === 404) {
        alert('ToDo not found');
      } else {
        alert('Error deleting ToDo');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Error deleting ToDo');
    }
  });
});



//display.html