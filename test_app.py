import unittest
from app import app

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_calculation(self):
        response = self.client.post("/", data={"m1": "90", "m2": "80", "m3": "70"})
        self.assertEqual(response.status_code, 200)
        
        html_content = response.data.decode()
        self.assertIn("Total: 240.0", html_content)
        self.assertIn("Average: 80.00", html_content)
        self.assertIn("Grade: B", html_content)

if __name__ == "__main__":
    unittest.main()
