# Calendar To-Do List

A web-based to-do list application with a calendar interface, built using Flask, SQLite, HTML, CSS, and JavaScript.

## Features

- **Calendar View:** Browse tasks by date using a monthly calendar.
- **Task Management:** Add, mark as done, and delete tasks for any day.
- **Sidebar Popup:** View and manage tasks for a selected date in a sidebar.
- **Overdue Notifications:** Get browser notifications for overdue tasks (requires permission).
- **Persistent Storage:** Tasks are stored in a local SQLite database.
- **Responsive Design:** Works on both desktop and mobile devices.

## Getting Started

### Prerequisites

- Python 3.x
- Flask (`pip install flask`)

### Setup

1. Clone or download this repository.
2. Install dependencies:
    ```
    pip install flask
    ```
3. Run the application:
    ```
    python app.py
    ```
4. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

### File Structure

- `app.py` - Flask backend and API.
- `tasks.db` - SQLite database (created automatically).
- `static/style.css` - Stylesheet for the app.
- `templates/index.html` - Main HTML template.
- `to-do list/README.md` - This file.

## Usage

- Click on any date in the calendar to view or add tasks for that day.
- Use the sidebar to add new tasks, mark them as done, or delete them.
- Navigate between months using the arrow buttons.
- Allow browser notifications to receive overdue task reminders.

