from django.contrib.auth.models import User
from django.test import TestCase
from tasks.models import Task


class TaskTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.testuser1 = User.objects.create_user(
            username='testuser1',
            password='abc123'
        )

        # Create a task
        cls.test_task = Task.objects.create(
            title='Task 1 Title',
            detail='Task 1 detail.',
            completed=False,
            user=cls.testuser1,
        )

    def test_task_content(self):
        task = Task.objects.get(id=1)
        expected_title = f'{task.title}'
        expected_detail = f'{task.detail}'
        expected_completed = f'{task.completed}'
        expected_user = f'{task.user}'
        self.assertEqual(expected_title, 'Task 1 Title')
        self.assertEqual(expected_detail, 'Task 1 detail.')
        self.assertEqual(expected_completed, 'False')
        self.assertEqual(expected_user, 'testuser1')