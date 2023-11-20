# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import VoiceFile




admin.site.register(VoiceFile)

