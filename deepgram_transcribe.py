import os
from dotenv import load_dotenv
load_dotenv()
import uuid
from deepgram import (
    DeepgramClient,
)
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
AUDIO_FILE = 'khutbah_bn.mp3'

def transcribe_audio(audio_file, input_language='en'):
    try:
        deepgram = DeepgramClient(api_key=DEEPGRAM_API_KEY)
        with open(audio_file, "rb") as audio_file:
            response = deepgram.listen.v1.media.transcribe_file(
                request=audio_file.read(),
                model="nova-3",
                smart_format=True,
                punctuate=True,
                language=input_language
            )

        result = response.results.channels[0].alternatives[0].transcript
        name = uuid.uuid4()
        print(result)
        with open(f"{name}.txt","w",encoding="utf-8", newline='\n') as file:
            file.write(result)
        return result

    except Exception as e:
        print(f"Exception: {e}")


# try:
#     deepgram = DeepgramClient(api_key=DEEPGRAM_API_KEY)
#     with open(AUDIO_FILE, "rb") as audio_file:
#             response = deepgram.listen.v1.media.transcribe_file(
#                 request=audio_file.read(),
#                 model="nova-3",
#                 smart_format=True,
#                 punctuate=True,
#                 language="bn"
#             )

#     result = response.results.channels[0].alternatives[0].transcript
#     name = uuid.uuid4()
#     print(result)
#     with open(f"{name}.txt","w",encoding="utf-8", newline='\n') as file:
#         file.write(result)
# except Exception as e:
#     print(f"Exception: {e}")