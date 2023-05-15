from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    mode = (("off","offline"),
            ("on","online")
            )
    eventtype_ =(("workshop","workshop"),
                 ("competition","competition")
                 )
    event_name = models.CharField(max_length=25,blank=False)
    event_dis = models.TextField(blank=False)
    event_prize = models.IntegerField(default=0,blank=False)
    event_pic = models.ImageField(upload_to='eventpics',blank=False)
    event_redirect_link = models.URLField()
    speaker_name = models.CharField(max_length=10,blank=False,default='')
    speaker_details = models.CharField(max_length=20,default='')
    speaker_pic = models.ImageField(upload_to='speakerpics',default='/defaultpic.jpg')
    registration_open_date = models.DateTimeField(default=datetime.now())
    registration_closing_date = models.DateTimeField(default=datetime.now())
    is_registration_closed= models.BooleanField(default=False)
    event_type=models.CharField(max_length=11,choices=eventtype_,default='workshop')
    max_participant_allowed =models.IntegerField(default=0)
    min_participant_allowed = models.IntegerField(default=0)
    event_mode=models.CharField(max_length=3,choices=mode,default='off')
    is_trending= models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.event_name
class RegisterEvent(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    is_registration_successfull_paid = models.BooleanField(default=False)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)