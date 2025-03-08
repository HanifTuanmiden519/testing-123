import unittest
from coe_number.fake_database import FakeDatabase

class TestFakeDatabase(unittest.TestCase):
    def test_fake_database(self):
        db = FakeDatabase()
        db.insert("user_1", {"name": "Alice"})
        self.assertEqual(db.get("user_1"), {"name": "Alice"})

if __name__ == '__main__':
    unittest.main()
