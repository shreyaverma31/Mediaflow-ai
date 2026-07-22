import pyttsx3

engine = pyttsx3.init()

text = """
Hello everyone.
Welcome to MediaFlow AI.
This project converts video to audio,
generates transcripts,
creates summaries,
and performs SEO analysis.
Thank you.
"""

engine.save_to_file(text, "speech.mp3")
engine.runAndWait()

print("MP3 created!")