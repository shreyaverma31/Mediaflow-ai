import os
import shutil
import whisper

os.environ["PATH"] += os.pathsep + r"C:\Users\sunil\Downloads\ffmpeg-2026-07-20-git-c23123630e-essentials_build\ffmpeg-2026-07-20-git-c23123630e-essentials_build\bin"

def transcribe_audio(job, audio_path):

    print("FFMPEG:", shutil.which("ffmpeg"))

    job.status = "Transcribing"
    job.speech_status = "Running"
    job.save()

    print("🎤 Speech Agent Started")

    model = whisper.load_model("base")

    result = model.transcribe(audio_path)

    transcript = result["text"]

    job.transcript = transcript
    job.speech_status = "Completed"
    job.save()

    print("✅ Speech Agent Finished")

    return transcript