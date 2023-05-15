# Generated by Django 4.2 on 2023-05-15 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_speaker_alter_event_registration_closing_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Speaker',
        ),
        migrations.AddField(
            model_name='event',
            name='speaker_details',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='event',
            name='speaker_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_closing_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 21, 44, 54, 365338)),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_open_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 21, 44, 54, 365338)),
        ),
    ]