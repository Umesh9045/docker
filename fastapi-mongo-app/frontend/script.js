const API = 'http://127.0.0.1:8000';

async function getTasks() {
    try {
        const res = await fetch(`${API}/tasks`);
        const tasks = await res.json();
        const list = document.getElementById("taskList");
        list.innerHTML = '';

        tasks.forEach(task => {
            const li = document.createElement("li");
            li.className = "list-group-item d-flex justify-content-between align-items-center";

            li.innerHTML = `
        ${task.name} 
        <span class="badge bg-info text-dark ms-2">Priority: ${task.priority}</span>
        <button class="btn btn-sm btn-secondary  ms-auto" onclick="deleteTask('${task.name}')">❌</button>
      `;
            list.appendChild(li);
        });
    } catch (err) {
        console.error("Error fetching tasks:", err);
    }
}

async function addTask() {
    const name = document.getElementById("name").value;
    const priority = parseInt(document.getElementById("priority").value);

    if (!name || isNaN(priority)) {
        alert("Please enter valid task details.");
        return;
    }

    await fetch(`${API}/tasks`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, priority })
    });

    document.getElementById("name").value = "";
    document.getElementById("priority").value = "";
    getTasks();
}

async function deleteTask(name) {
    await fetch(`${API}/tasks/${name}`, { method: 'DELETE' });
    getTasks();
}

getTasks(); // Load tasks on start
