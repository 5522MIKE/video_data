# Generated by Django 3.1 on 2020-08-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0019_auto_20200824_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='illegalstatistics',
            name='videoId',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='trafficflow',
            name='videoId',
            field=models.IntegerField(default='1'),
        ),
    ]