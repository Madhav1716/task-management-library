# tests/test_task.py

import unittest
from task_management.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        # Test task creation
        task = Task("Test Task", "This is a test task", "2024-05-01", "High")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task")
        self.assertEqual(task.due_date, "2024-05-01")
        self.assertEqual(task.priority, "High")

    def test_mark_task_as_completed(self):
        # Test marking task as completed
        task = Task("Test Task", "This is a test task", "2024-05-01", "High")
        self.assertFalse(task.completed)  # Task should be initially incomplete
        task.mark_as_completed()
        self.assertTrue(task.completed)  # Task should be marked as completed

    def test_update_task_details(self):
        # Test updating task details
        task = Task("Test Task", "This is a test task", "2024-05-01", "High")
        task.update_task(title="Updated Task", description="Updated description", due_date="2024-05-02", priority="Low")
        self.assertEqual(task.title, "Updated Task")
        self.assertEqual(task.description, "Updated description")
        self.assertEqual(task.due_date, "2024-05-02")
        self.assertEqual(task.priority, "Low")

if __name__ == '__main__':
    unittest.main()
