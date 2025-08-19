from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
tasks_file = 'tasks.json'

def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(tasks_file, 'w') as f:
        json.dump(tasks, f, indent=4)

@app.route('/')
def index():
    tasks = load_tasks()
    tasks.sort(key=lambda x: (x['due_date'], x['due_time']))

    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if t['status'] == "Completed")
    pending_tasks = total_tasks - completed_tasks
    progress = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0

    return render_template(
        'index.html',
        tasks=tasks,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
        progress=progress
    )

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        tasks = load_tasks()
        new_task = {
            "id": len(tasks) + 1,
            "name": request.form['name'],
            "description": request.form.get('description', ''),
            "due_date": request.form['due_date'],
            "due_time": request.form['due_time'],
            "status": "Pending"
        }
        tasks.append(new_task)
        save_tasks(tasks)
        return redirect('/')
    return render_template('add_task.html')

@app.route('/task/<int:task_id>')
def task_detail(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    return render_template('task_detail.html', task=task)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if request.method == 'POST':
        task['name'] = request.form['name']
        task['description'] = request.form.get('description', '')
        task['due_date'] = request.form['due_date']
        task['due_time'] = request.form['due_time']
        save_tasks(tasks)
        return redirect('/')
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return redirect('/')

@app.route('/toggle_status/<int:task_id>')
def toggle_status(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['status'] = "Completed" if task['status'] == "Pending" else "Pending"
        save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
