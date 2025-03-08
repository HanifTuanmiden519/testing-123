import unittest
from unittest.mock import Mock

class EmailService:
    def send_email(self, recipient, message):
        pass  

class TestEmailService(unittest.TestCase):
    def test_send_email_mock(self):
        email_service = EmailService()
        email_service.send_email = Mock()

        email_service.send_email("test@example.com", "Hello!")
        email_service.send_email.assert_called_with("test@example.com", "Hello!")

if __name__ == '__main__':
    unittest.main()
