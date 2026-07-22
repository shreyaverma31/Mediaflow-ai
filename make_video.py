from moviepy import AudioFileClip, ColorClip

audio = AudioFileClip("speech.mp3")

video = (
    ColorClip(size=(1280, 720), color=(0, 0, 0), duration=audio.duration)
    .with_audio(audio)
)

video.write_videofile("test_video.mp4", fps=24)