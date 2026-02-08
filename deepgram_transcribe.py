import os
from dotenv import load_dotenv
load_dotenv()
from deepgram import (
    DeepgramClient,
)
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
AUDIO_FILE = 'khutbah_eng.mp3'

def transcribe():
    try:
        deepgram = DeepgramClient(api_key=DEEPGRAM_API_KEY)
        with open(AUDIO_FILE, "rb") as audio_file:
            response = deepgram.listen.v1.media.transcribe_file(
                request=audio_file.read(),
                model="nova-3",
                smart_format=True,
                punctuate=True
            )
            result = response.results.channels[0].alternatives[0].transcript

        with open("response.txt","w",encoding="utf-8", newline='\n') as file:
            file.write(result)
        return

    except Exception as e:
        print(f"Exception: {e}")


transcribe()