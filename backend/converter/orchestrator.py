from .models import VideoJob

from .agents.audio_agent import extract_audio
from .agents.speech_agent import transcribe_audio
from .agents.summary_agent import generate_summary
from .agents.seo_agent import generate_seo
from .agents.hook_agent import generate_hooks

import traceback


def process_pipeline(job_id):

    try:
        job = VideoJob.objects.get(id=job_id)

        print("🚀 Pipeline Started")

        audio = extract_audio(job)

        transcript = transcribe_audio(job, audio)

        summary = generate_summary(job, transcript)

        seo = generate_seo(job)

        hooks = generate_hooks(job)

        job.status = "Completed"
        job.save()

        print("✅ Pipeline Finished")

    except Exception:
        traceback.print_exc()

        job = VideoJob.objects.get(id=job_id)
        job.status = "Failed"
        job.save()