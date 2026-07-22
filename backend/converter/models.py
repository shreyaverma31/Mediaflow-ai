from django.db import models

class VideoJob(models.Model):
    STATUS_CHOICES = [
        ("Uploaded", "Uploaded"),
        ("Extracting Audio", "Extracting Audio"),
        ("Transcribing", "Transcribing"),
        ("Summarizing", "Summarizing"),
        ("Completed", "Completed"),
    ]

    video = models.FileField(upload_to="uploads/")

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Uploaded",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    audio_path = models.TextField(blank=True)
    transcript = models.TextField(blank=True)
    summary = models.TextField(blank=True)

    audio_status = models.CharField(max_length=50, default="Waiting")
    speech_status = models.CharField(max_length=50, default="Waiting")
    summary_status = models.CharField(max_length=50, default="Waiting")
    seo_status = models.CharField(max_length=50, default="Waiting")
    hook_status = models.CharField(max_length=50, default="Waiting")

    # NEW FIELDS
    seo_result = models.TextField(blank=True)
    hook_result = models.TextField(blank=True)

    def __str__(self):
        return f"Job {self.id} - {self.status}"