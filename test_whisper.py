# test_whisper.py
import os
import whisper

print("Loading model...")
model = whisper.load_model("base")

print("Transcribing...")
result = model.transcribe("media/audio/17.mp3")

print(result["text"])