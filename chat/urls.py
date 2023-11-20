from django.urls import path
from .views import TextToAudioAPI

urlpatterns = [
    path('text/', TextToAudioAPI.as_view(), name='voice_chat'),
]
