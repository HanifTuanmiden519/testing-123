import unittest

class Logger:
    def log(self, message):
        pass  

class UserService:
    def __init__(self, logger):
        self.logger = logger

    def create_user(self, name):
        self.logger.log(f"User {name} created")
        return {"name": name}

class TestUserService(unittest.TestCase):
    def test_create_user_with_dummy_logger(self):
        dummy_logger = Logger()
        service = UserService(dummy_logger)
        self.assertEqual(service.create_user("Alice")["name"], "Alice")

if __name__ == '__main__':
    unittest.main()
