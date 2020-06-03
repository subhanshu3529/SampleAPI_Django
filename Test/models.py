from django.db import models
import pytz
# Create your models here.
# User and ActivityPeriod models
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

class User(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=32, choices=TIMEZONES,)

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id =models.ForeignKey(User, on_delete=models.CASCADE)