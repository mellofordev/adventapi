# Generated by Django 4.2 on 2023-05-15 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_event_speaker_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='registration_closing_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 21, 53, 8, 7143)),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_open_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 21, 53, 8, 7143)),
        ),
    ]