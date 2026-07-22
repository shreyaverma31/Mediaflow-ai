from django.test import TestCase
from rest_framework.test import APIClient


class HomeTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_home(self):

        response = self.client.get("/api/")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            response.data["project"],
            "MediaFlow AI"
        )