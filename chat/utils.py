import json
import time
from pathlib import Path

import requests
from django.core.files import File
from openai import OpenAI

from AudioAI.settings import BASE_DIR
from chat.models import VoiceFile
from django.conf import settings

OPENAI_SECRET_KEY = settings.OPENAI_SECRET_KEY
SOURCE_URL = settings.SOURCE_URL
TALKS_URL = settings.TALKS_URL
DID_SECRET_KEY = settings.DID_SECRET_KEY
client = OpenAI(api_key=OPENAI_SECRET_KEY)


class TextToSpeechService:
    def __init__(self):
        pass

    def get_answer(self, text):
        print(text, "text")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content

    def text_to_speech(self,request, text):
        answer = self.get_answer(text)
        speech_file_path = BASE_DIR / 'media' / "speech.mp3"

        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=answer
        )
        response.stream_to_file(speech_file_path)

        speech_model = VoiceFile(text=text)
        speech_model.file_path.save('speech.mp3', File(open(speech_file_path, 'rb')))
        speech_model.save()
        speech_model.save()
        host = request.get_host() if request else "localhost"

        # Return the complete URL with host
        return f"{host}{speech_model.file_path.url}"

