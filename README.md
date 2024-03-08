# Task Management System

This is a simple task management system implemented in Python. It allows users to register, log in, add tasks, view tasks, and display statistics. Tasks are stored in a text file (`tasks.txt`) and user information is stored in another text file (`user.txt`).
The default username and password have been initially set to 'admin and 'password', respectively.

## Features

- User registration: Admin users can register with a username and password.
- User login: Registered users can log in with their username and password.
- Add tasks: Users can add tasks, including the assigned user, title, description, due date, and completion status.
- View all tasks: Users can view all tasks stored in the system.
- View my tasks: Users can view tasks assigned to them.
- Generate report: Admin users can generate reports, two text files will be generated 'tasks_overview.txt' and 'user_overview.txt'.
  - task_overview.txt: Will contain total number of tasks, total number of completed tasks, total number of uncompleted tasks, total number of tasks that haven't been completed and that are overdue. percentage of tasks        that are incomplete, and the percentage of tasks that are overdue.
  - user_overview.txt: Will contain the number of user registered, the total number of tasks that have been generated and tracked, and for each user it will show the total number of task assigned to that user, percentage      of the total number of tasks that have been assigned to that user, percentage of the tasks assigned to that user that have been completed, percentage of the tasks assigned that must still be completed, and percentage      of the tasks that have not yet been completed and overdue.
- Display statistics: Admin users can display statistics about the number of users and tasks in the system.

## Usage

1. Clone the repository:
2. Run the `task_manager.py` file:
3. Follow the on-screen prompts to use the system.

## File Structure

- `task_manager.py`: The main Python script implementing the task management system.
- `tasks.txt`: Text file storing task data.
- `user.txt`: Text file storing user data.

## Dependencies

This project does not have any external dependencies beyond Python 3.x
