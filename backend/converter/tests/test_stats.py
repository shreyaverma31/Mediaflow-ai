from django.test import TestCase
from rest_framework.test import APIClient


class StatsTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_stats(self):

        response = self.client.get("/api/stats/")

        self.assertEqual(response.status_code, 200)

        self.assertIn("uploads", response.data)
        self.assertIn("processing", response.data)
        self.assertIn("completed", response.data)