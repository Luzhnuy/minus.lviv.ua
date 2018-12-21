from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Channels(models.Model):
    user = models.ForeignKey(User)
    is_active = models.BooleanField()
    # count_new_messages = models.IntegerField()
