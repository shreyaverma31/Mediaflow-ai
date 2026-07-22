from django.test import TestCase

from converter.models import VideoJob
from converter.orchestrator import process_pipeline


class PipelineTest(TestCase):

    def test_pipeline(self):

        job = VideoJob.objects.create(
            video="uploads/test.mp4",
            status="Queued"
        )

        process_pipeline(job)

        job.refresh_from_db()

        self.assertEqual(job.status, "Completed")