# Task Management Library

The task_management_library package is a Python library designed to facilitate task management functionalities within software applications. It provides a simple and flexible interface for creating, updating, and organizing tasks, enabling developers to integrate task management capabilities seamlessly into their projects.

## Features

- **Task Creation**: Allows users to create new tasks with customizable attributes such as title, description, due date, and priority.
- **Task Modification**: Enables users to update existing tasks, including modifying their title, description, due date, or priority.

- **Task Deletion**: Provides functionality to delete tasks from the task list, allowing for the removal of completed or obsolete tasks.

- **Task Organization**: Supports the organization of tasks into categories or projects, enhancing workflow management and task prioritization.

- **Data Persistence**: Offers options for data persistence, allowing tasks to be saved and retrieved from various storage mechanisms such as databases or file systems.

## Installation

You can install the task_management_library package using pip:

```bash
pip install task_management_library
```

from task_management.task import Task

# Create a new task

task = Task("Complete assignment", "Finish project by the end of the week", "2024-05-05", "High")

# Print task details

print(task)
