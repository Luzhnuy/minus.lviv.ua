from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# class AuthUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # username = models.CharField(unique=True, max_length=30)
#     # first_name = models.CharField(max_length=30)
#     # last_name = models.CharField(max_length=30)
#     # email = models.CharField(max_length=75)
#     # password = models.CharField(max_length=128)
#     # is_staff = models.IntegerField()
#     # is_active = models.IntegerField()
#     # is_superuser = models.IntegerField()
#     # last_login = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     # date_joined = models.DateTimeField(auto_now_add=True, blank=True)
#     is_business = models.BooleanField(default=0)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user'
#
# @receiver(post_save, sender=User)
# def create_auth_user(sender, instance, created, **kwargs):
#     if created:
#         AuthUser.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_auth_user(sender, instance, **kwargs):
#     instance.authuser.save()
#

class FriendsFriendship(models.Model):
    user = models.ForeignKey(User,on_delete="CASCADE")

    class Meta:
        managed = True
        db_table = 'friends_friendship'


class FriendsFriendshipFriends(models.Model):
    from_friendship_id = models.IntegerField()
    to_friendship_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'friends_friendship_friends'
        unique_together = (('from_friendship_id', 'to_friendship_id'),)


class FriendsFriendshiprequest(models.Model):
    from_user_id = models.IntegerField()
    to_user_id = models.IntegerField()
    message = models.CharField(max_length=200)
    created = models.DateTimeField()
    accepted = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'friends_friendshiprequest'
        unique_together = (('to_user_id', 'from_user_id'),)


class FriendsUserblocks(models.Model):
    user = models.ForeignKey(User,on_delete="CASCADE")


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


class UserActivitys(models.Model):
    activity_type = (
        ('l','like'),
        ('d','dislike'),
        ('c', 'comment'),
    )

    type = models.CharField(choices=activity_type,null=True,max_length=255)
    from_user = models.ForeignKey(User,on_delete="PROTECT")
    to_user_id = models.IntegerField()
    activity_to = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'useractivitys'


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    avatar = models.CharField(max_length=128, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    hide_birthdate = models.IntegerField(blank=True, null=True)
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
    is_business = models.BooleanField(default=0)
    is_user_online = models.BooleanField(default=0)

    class Meta:
        managed = True
        db_table = 'userprofile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Userprofile.objects.create(user=instance,banned = 0,hide_birthdate = 0,is_admin_subscribed = 0,seen_rules = 0)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class UsersStaffticket(models.Model):
    user = models.ForeignKey(User,on_delete="PROTECT")
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
    user = models.ForeignKey(User,on_delete="PROTECT")
    rating = models.IntegerField()
    average_minus_rating = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'users_userrating'







@receiver(post_save, sender=User)
def create_user_rating(sender, instance, created, **kwargs):
    if created:
        UsersUserrating.objects.create(user=instance,rating = 0,average_minus_rating = 0)
