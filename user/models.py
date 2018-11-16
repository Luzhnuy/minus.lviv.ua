from django.db import models
from django.contrib.auth.models import User

class AuthUser(models.Model):

    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        managed = True
        db_table = 'auth_user'

class FriendsUserblocks(models.Model):
    user = models.ForeignKey(User)

    class Meta:
        managed = True
        db_table = 'friends_userblocks'


class FriendsUserblocksBlocks(models.Model):
    userblocks_id = models.IntegerField()
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = True
        db_table = 'friends_userblocks_blocks'
        unique_together = (('userblocks_id', 'user_id'),)

class Userprofile(models.Model):
    user = models.ForeignKey(User)
    gender = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    avatar = models.CharField(max_length=128, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    hide_birthdate = models.IntegerField()
    icq = models.CharField(max_length=10, blank=True, null=True)
    jabber = models.CharField(max_length=128, blank=True, null=True)
    skype = models.CharField(max_length=128, blank=True, null=True)
    website = models.CharField(max_length=128, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    is_admin_subscribed = models.IntegerField()
    status_title = models.CharField(max_length=20, blank=True, null=True)
    status_css = models.CharField(max_length=20, blank=True, null=True)
    banned = models.IntegerField()
    banned_until = models.DateField(blank=True, null=True)
    seen_rules = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'userprofile'


class UsersStaffticket(models.Model):
    user = models.ForeignKey(User)
    content_type_id = models.IntegerField()
    object_id = models.IntegerField()
    url = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField()
    is_done = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'users_staffticket'


class UsersUseractivity(models.Model):
    last_activity_ip = models.CharField(max_length=15)
    last_activity_date = models.DateTimeField()
    user_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'users_useractivity'


class UsersUserrating(models.Model):
    user = models.ForeignKey(User)
    rating = models.IntegerField()
    average_minus_rating = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'users_userrating'
