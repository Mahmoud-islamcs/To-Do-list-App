# Taskify - Full-Stack To-Do List Web App

A modern, responsive **To-Do List application** built with **Flask backend** and **vanilla JavaScript frontend**, featuring task management, progress tracking, and celebratory animations.

---

## ✅ Features

- Add new tasks with **name, description, due date, and time**
- Mark tasks as **complete/incomplete**
- Edit existing tasks
- Delete tasks
- **Progress tracking** with a visual progress bar
- Task statistics: **Total, Completed, Pending**
- **Confetti animation** when all tasks are completed
- Persistent data storage via **JSON file**
- Responsive design for desktop and mobile
- Smooth **hover effects** and **animations** with Bootstrap

---

## 📂 Project Structure

taskify/
├── app.py # Flask backend server
├── tasks.json # JSON file storing tasks (auto-created)
├── requirements.txt # Python dependencies
├── templates/
│ ├── index.html
│ ├── add_task.html
│ ├── edit_task.html
│ └── task_detail.html
└── static/
├── css/style.css # Custom styling
└── js/script.js # Frontend scripts

yaml
Copy
Edit

---

## ⚡ Setup Instructions

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone or download the project:

```bash
git clone <repository-url>
cd taskify
Install Python dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask server:

bash
Copy
Edit
python app.py
Open your browser and navigate to:

cpp
Copy
Edit
http://127.0.0.1:5000
🖥️ How It Works
Backend (Flask)
Stores tasks in tasks.json

Provides CRUD operations: add, edit, delete, toggle status

Calculates task stats: total, completed, pending

Computes progress percentage for progress bar

Frontend (JavaScript + Bootstrap)
Dynamically updates UI on task changes

Confetti animation triggers when all tasks are completed

Responsive and mobile-friendly

Smooth hover and animation effects

Data Flow
User interacts with frontend

Frontend sends request to Flask backend

Backend updates tasks.json and sends response

Frontend updates task list, stats, and progress bar

🎨 Task Management & Progress
Add Task: Fill form and submit

Edit Task: Click "Edit" on a task

Delete Task: Click "Delete" icon

Complete Task: Toggle "Complete/Undo" button

Progress Bar: Updates in real-time based on completed tasks

Celebration: Confetti animation appears when all tasks are completed

🛠️ Development
Modify app.py to add backend features

Update script.js for new frontend interactions

Customize style.css for animations and UI enhancements

⚠️ Troubleshooting
Tasks not saving: Ensure tasks.json is writable

Port in use: Change Flask port in app.py

Frontend not updating: Clear browser cache or refresh page
```
