import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

from tts import speak
from intent handler import get intent
from response generator import generate_response

MODEL PATH = "models/vosk-model-small-hi-0.22"16000)

# Load ASR model

model = Model (MODEL PATH)
recognizer = KaldiRecognizer (model,

# Queue to safely pass text from callback → main loop 
text_queue = queue.Queue ()

# Audio callback (ASR ONLY)
def callback(indata, frames, time, status):
    if recognizer.AcceptWaveform(indata):
        result = json.loads (recognizer.Result())
        text = result.get("text", "")
        if text:
            text_queue.put(text)

print(" Hindi Voice Assistant Started (say ' to exit)")

with sd.RawInputStream(
    samplerate=16000, 
    blocksize=8000,
    dtype='int16', 
    channels=1,
    callback=callback):

while True:
    #Wait for recognized text text = text_queue.get()
    print("You said:", text)

    intent = get_intent (text)

    response = generate_response (intent)