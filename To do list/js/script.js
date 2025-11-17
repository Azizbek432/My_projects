const taskInput = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const taskList = document.getElementById("taskList");

function saveTasks() {
  const tasks = [];
  document.querySelectorAll("li").forEach(item => {
    tasks.push({
      text: item.querySelector("span").textContent,
      completed: item.classList.contains("completed")
    });
  });
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
  const saved = JSON.parse(localStorage.getItem("tasks")) || [];
  saved.forEach(task => addTask(task.text, task.completed));
}

function addTask(text, completed = false) {
  if (text.trim() === "") return;
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.textContent = text;
  li.appendChild(span);

  const delBtn = document.createElement("button");
  delBtn.textContent = "🗑️";
  delBtn.className = "delete";
  delBtn.onclick = () => {
    li.remove();
    saveTasks();
  };
  li.appendChild(delBtn);

  li.onclick = (e) => {
    if (e.target.tagName !== "BUTTON") {
      li.classList.toggle("completed");
      saveTasks();
    }
  };

  if (completed) li.classList.add("completed");

  taskList.appendChild(li);
  taskInput.value = "";
  saveTasks();
}

addBtn.onclick = () => addTask(taskInput.value);
window.addEventListener("load", loadTasks);
