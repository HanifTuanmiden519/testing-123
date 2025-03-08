import unittest
from unittest.mock import MagicMock

class UserService:
    def get_user(self, user_id):
        pass  

class TestUserService(unittest.TestCase):
    def test_get_user_stub(self):
        service = UserService()
        service.get_user = MagicMock(return_value={"id": 1, "name": "Alice"})
        self.assertEqual(service.get_user(1)["name"], "Alice")

if __name__ == '__main__':
    unittest.main()
