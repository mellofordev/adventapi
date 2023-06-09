# Generated by Django 4.2 on 2023-05-15 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_event_stripe_prize_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='is_competition',
        ),
        migrations.RemoveField(
            model_name='event',
            name='is_workshop',
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('workshop', 'workshop'), ('competition', 'competition')], default='workshop', max_length=11),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_closing_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 22, 33, 9, 183209)),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_open_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 22, 33, 9, 183209)),
        ),
    ]
