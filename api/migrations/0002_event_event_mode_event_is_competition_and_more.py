# Generated by Django 4.2 on 2023-04-25 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_mode',
            field=models.CharField(choices=[('off', 'offline'), ('on', 'online')], default='off', max_length=3),
        ),
        migrations.AddField(
            model_name='event',
            name='is_competition',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='is_registration_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='is_trending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='is_workshop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='max_participant_allowed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='min_participant_allowed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='registration_closing_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 25, 13, 13, 22, 12691)),
        ),
        migrations.AddField(
            model_name='event',
            name='registration_open_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 25, 13, 13, 22, 12691)),
        ),
    ]
