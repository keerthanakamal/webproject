from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), 'tasks.db')

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                text TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks/<date>', methods=['GET', 'POST', 'DELETE'])
def tasks(date):
    if request.method == 'GET':
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute('SELECT id, text, done FROM tasks WHERE date = ?', (date,))
            tasks = [{'id': row[0], 'text': row[1], 'done': bool(row[2])} for row in c.fetchall()]
        return jsonify(tasks)
    elif request.method == 'POST':
        data = request.get_json()
        text = data.get('text', '').strip()
        if not text:
            return jsonify({'error': 'Empty task'}), 400
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute('INSERT INTO tasks (date, text, done) VALUES (?, ?, 0)', (date, text))
            conn.commit()
            task_id = c.lastrowid
        return jsonify({'id': task_id, 'text': text, 'done': False})
    elif request.method == 'DELETE':
        data = request.get_json()
        task_id = data.get('id')
        if not task_id:
            return jsonify({'error': 'No task id'}), 400
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            conn.commit()
        return jsonify({'success': True})

@app.route('/tasks/done/<int:task_id>', methods=['POST'])
def mark_done(task_id):
    data = request.get_json()
    done = 1 if data.get('done') else 0
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('UPDATE tasks SET done = ? WHERE id = ?', (done, task_id))
        conn.commit()
    return jsonify({'success': True})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
