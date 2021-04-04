from django.test import TestCase
from .models import Email

class EmailTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create an email
        test_email = Email.objects.create(
            from_email='test@email.com',
            subject='Hello Test',
            message='Email content...'
        )
        test_email.save()

    def test_email_content(self):
        email = Email.objects.get(id=1)
        expected_from_email = f'{email.from_email}'
        expected_subject = f'{email.subject}'
        expected_message = f'{email.message}'
        self.assertEqual(expected_from_email, 'test@email.com')
        self.assertEqual(expected_subject, 'Hello Test')
        self.assertEqual(expected_message, 'Email content...')