# Generated by Django 3.1 on 2020-08-23 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_speedlimit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video_name',
            new_name='video_path',
        ),
    ]
