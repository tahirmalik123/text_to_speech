from rest_framework import generics
from rest_framework.response import Response

from .serializers import VoiceSerializer
from chat.utils import TextToSpeechService


class TextToAudioAPI(generics.GenericAPIView):
    serializer_class = VoiceSerializer

    def post(self, request, *args, **kwargs):
        text = request.data.get("text")
        answer = TextToSpeechService().text_to_speech(request, text)
        return Response({"message": 'success', "video_url": answer}, status=200)
