# task_management/task.py

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def update_task(self, title=None, description=None, due_date=None, priority=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if priority is not None:
            self.priority = priority

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - Priority: {self.priority}, Due: {self.due_date}, Status: {status}"
