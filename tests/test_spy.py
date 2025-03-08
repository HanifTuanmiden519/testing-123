import unittest
from unittest.mock import MagicMock

class APIClient:
    def fetch_data(self, url):
        pass  

class TestAPIClient(unittest.TestCase):
    def test_api_call_spy(self):
        client = APIClient()
        client.fetch_data = MagicMock(return_value={"status": "ok"})

        client.fetch_data("https://api.example.com/data")
        self.assertEqual(client.fetch_data.call_count, 1)

if __name__ == '__main__':
    unittest.main()
