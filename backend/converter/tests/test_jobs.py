from django.test import TestCase
from rest_framework.test import APIClient


class JobsTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_jobs_endpoint(self):

        response = self.client.get("/api/jobs/")

        self.assertEqual(response.status_code, 200)