# Generated by Django 3.2.23 on 2023-11-20 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_voicefile_video_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voicefile',
            old_name='video_file',
            new_name='text',
        ),
    ]
