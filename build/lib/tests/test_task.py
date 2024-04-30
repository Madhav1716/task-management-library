# tests/test_task.py

import unittest
from task_management.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test Task", "This is a test task", "2024-05-01", "High")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task")
        self.assertEqual(task.due_date, "2024-05-01")
        self.assertEqual(task.priority, "High")

if __name__ == '__main__':
    unittest.main()
