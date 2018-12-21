from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Channels(models.Model):
    user = models.ForeignKey(User)
    is_active = models.BooleanField()
    # count_new_messages = models.IntegerField()


class NewMessagesChannels(models.Model):
    count = models.IntegerField(null=True,blank=True)
    frm_user = models.ForeignKey(User)
    to_user = models.IntegerField()
