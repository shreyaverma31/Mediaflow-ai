from rest_framework.decorators import api_view
from rest_framework.response import Response
import threading

from .orchestrator import process_pipeline
from .models import VideoJob
from .serializers import VideoJobSerializer


@api_view(["GET"])
def home(request):
    return Response({
        "project": "MediaFlow AI",
        "version": "2.0",
        "status": "Running",
        "pipeline": "Multi-Agent AI Pipeline",
        "agents": [
            "Audio Agent",
            "Speech Agent",
            "Summary Agent",
            "SEO Agent",
            "Hook Agent"
        ]
    })


@api_view(["POST"])
def upload_video(request):

    file = request.FILES.get("video")

    if not file:
        return Response(
            {"error": "No file uploaded"},
            status=400
        )

    job = VideoJob.objects.create(
        video=file,
        status="Queued"
    )

    threading.Thread(
        target=process_pipeline,
        args=(job.id,),
        daemon=True
    ).start()

    return Response(
        VideoJobSerializer(job).data,
        status=201
    )


@api_view(["GET"])
def jobs(request):

    jobs = VideoJob.objects.order_by("-created_at")

    serializer = VideoJobSerializer(
        jobs,
        many=True
    )

    return Response(serializer.data)


@api_view(["GET"])
def job_detail(request, job_id):

    try:
        job = VideoJob.objects.get(id=job_id)

        return Response({
            "id": job.id,
            "status": job.status,
            "created_at": job.created_at,
            "audio_path": job.audio_path,

            "transcript": job.transcript,
            "summary": job.summary,

            "seo": job.seo_result,
            "hooks": job.hook_result,

            "audio_status": job.audio_status,
            "speech_status": job.speech_status,
            "summary_status": job.summary_status,
            "seo_status": job.seo_status,
            "hook_status": job.hook_status,
        })

    except VideoJob.DoesNotExist:
        return Response(
            {"error": "Job not found"},
            status=404
        )


@api_view(["GET"])
def stats(request):

    uploads = VideoJob.objects.count()

    processing = VideoJob.objects.filter(
        status__in=[
            "Queued",
            "Extracting Audio",
            "Transcribing",
            "Summarizing",
            "SEO Analysis",
            "Generating Hooks",
        ]
    ).count()

    completed = VideoJob.objects.filter(
        status="Completed"
    ).count()

    failed = VideoJob.objects.filter(
        status="Failed"
    ).count()

    return Response({
        "uploads": uploads,
        "processing": processing,
        "completed": completed,
        "failed": failed,
        "agents": 5
    })