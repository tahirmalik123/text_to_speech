# Generated by Django 3.2.23 on 2023-11-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voicefile',
            name='video_file',
            field=models.TextField(blank=True, null=True),
        ),
    ]
