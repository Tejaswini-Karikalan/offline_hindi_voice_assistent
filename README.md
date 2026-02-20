# offline_hindi_voice_assistent
An offline Hindi voice assistant built on Raspberry Pi that performs Speech-to-Text, intent recognition, and Text-to-Speech locally. Unlike cloud assistants like Amazon Alexa, it ensures privacy, low latency, and real-time response. It supports regional language interaction for smart homes, education, and secure edge-AI applications.
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

#tts

import os
text = text.replace("\n", "").strip() os.system("pactl set-sink-mute @DEFAULT SINK@ 0") time.sleep(0.4)
os.system('espeak-ng -q" "') os.system(f'espeak-ng -v hi -s 120 -p 50 "(text}"')

#intent_handler

def get_intent(text):
    text = text.strip()

    if "नमस्ते" in text:
        return "greeting"

    elif "समय" in text:
        return "time"

    elif "तारीख" in text:
        return "date"

    elif "मदद" in text:
        return "help"

    elif "बंद" in text:
        return "exit"

    elif "धन्यवाद" in text:
        return "thanks"

    elif "नाम" in text:
        return "name"

    elif "स्थिति" in text:
        return "status"

    elif "आवाज़" in text:
        return "audio"

    elif "शुरू" in text:
        return "start"

    elif "रुको" in text:
        return "pause"

    elif "दोहराओ" in text:
        return "repeat"

    elif "साफ" in text:
        return "clear"

    elif "कहाँ" in text:
        return "location"

    elif "ठीक" in text:
        return "ok"

    else:
        return "unknown"
