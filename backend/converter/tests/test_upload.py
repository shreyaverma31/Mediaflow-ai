from django.test import TestCase
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile


class UploadTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_video_upload(self):

        video = SimpleUploadedFile(
            "sample.mp4",
            b"fake video",
            content_type="video/mp4"
        )

        response = self.client.post(
            "/api/upload/",
            {"video": video},
            format="multipart"
        )

        self.assertEqual(response.status_code, 201)