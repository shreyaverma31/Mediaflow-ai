import os
import subprocess


def extract_audio(job):

    job.status = "Extracting Audio"
    job.audio_status = "Running"
    job.save()

    print("Audio Agent Started")

    os.makedirs("media/audio", exist_ok=True)

    audio_path = os.path.join(
        "media",
        "audio",
        f"{job.id}.mp3"
    )

    command = [
        r"C:\Users\sunil\Downloads\ffmpeg-2026-07-20-git-c23123630e-essentials_build\ffmpeg-2026-07-20-git-c23123630e-essentials_build\bin\ffmpeg.exe",
        "-i",
        job.video.path,
        "-vn",
        "-acodec",
        "mp3",
        "-y",
        audio_path,
    ]

    print(command)

    subprocess.run(command, check=True)

    job.audio_path = audio_path
    job.audio_status = "Completed"
    job.save()

    print("Audio Agent Finished")

    return audio_path