from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save tasks to file
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form['task']
    tasks = load_tasks()
    tasks.append({'task': task_text, 'completed': False})
    save_tasks(tasks)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
    save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
