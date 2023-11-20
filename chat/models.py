from django.db import models


class VoiceFile(models.Model):
    text = models.TextField(null=True, blank=True)
    file_path = models.FileField(upload_to='speeches/', null=True, blank=True)


    def __str__(self):
        return f"VoiceFile {self.id}"