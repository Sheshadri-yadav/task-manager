function updateTask(taskId) {
    const url = `/update/${taskId}`;
    const options = {
        method: 'PUT', // Use PUT method
        headers: {
            'Content-Type': 'application/json' // Set content type
        }
    };

    fetch(url, options)
        .then(response => {
            if (response.ok) {
                return response.json(); // Parse response JSON if successful
            } else {
                throw new Error('Failed to update task'); // Throw error if request fails
            }
        })
        .then(data => {
            console.log('Task updated successfully:', data);
            // Update HTML content based on the updated tasks
            const tbody = document.querySelector('tbody');
            tbody.innerHTML = ''; // Clear existing rows
            data.tasks.forEach(task => {
                tbody.innerHTML += `
                    <tr>
                        <td>${task.task_id}</td>
                        <td>${task.task_title}</td>
                        <td>${task.task_desc}</td>
                        <td>${task.due_date}</td>
                        <td>${task.due_time}</td>
                        <td>${task.task_status}</td>
                        <td>
                            <button onclick="updateTask(${task.task_id})">Mark as Completed</button>
                        </td>
                        <td>
                           <button onclick="deleteTask(${task.task_id})">Delete Task</button>

                        </td>
                    </tr>
                `;
            });
        })
        .catch(error => {
            console.error('Error updating task:', error); // Log error message
        });
}





function deleteTask(taskId) {
    const url = `/delete/${taskId}`;
    const options = {
        method: 'DELETE', // Use DELETE method
        headers: {
            'Content-Type': 'application/json' // Set content type
        }
    };

    fetch(url, options)
        .then(response => {
            if (response.ok) {
                return response.json(); // Parse response JSON if successful
            } else {
                throw new Error('Failed to delete task'); // Throw error if request fails
            }
        })
        .then(data => {
            console.log('Task deleted successfully:', data);
             // Update HTML content based on the updated tasks
            const tbody = document.querySelector('tbody');
            tbody.innerHTML = ''; // Clear existing rows
            data.tasks.forEach(task => {
                tbody.innerHTML += `
                    <tr>
                        <td>${task.task_id}</td>
                        <td>${task.task_title}</td>
                        <td>${task.task_desc}</td>
                        <td>${task.due_date}</td>
                        <td>${task.due_time}</td>
                        <td>${task.task_status}</td>
                        <td>
                            <button onclick="updateTask(${task.task_id})">Mark as Completed</button>
                        </td>
                        <td>
                           <button onclick="deleteTask(${task.task_id})">Delete Task</button>

                        </td>
                    </tr>
                `;
            });

             })
        .catch(error => {
            alert('Error deleting task:', error); // Log error message

        });
}

