from rest_framework import serializers
from .models import VoiceFile


class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceFile
        fields = ('text', )
