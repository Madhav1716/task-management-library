# task_management/task.py

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"{self.title} - Priority: {self.priority}, Due: {self.due_date}"
