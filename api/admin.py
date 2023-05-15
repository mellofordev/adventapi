from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Event)
admin.site.site_header='Advent Admin'
admin.site.site_title='Advent Admin'