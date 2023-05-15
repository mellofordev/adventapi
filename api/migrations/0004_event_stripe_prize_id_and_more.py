# Generated by Django 4.2 on 2023-05-05 03:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_alter_event_registration_closing_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='stripe_prize_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_closing_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 9, 5, 13, 308782)),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_open_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 9, 5, 13, 308782)),
        ),
        migrations.CreateModel(
            name='RegisterEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_registration_successfull_paid', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.event')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]