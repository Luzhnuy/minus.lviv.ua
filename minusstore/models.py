from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import os


class MinusstoreCommentnotify(models.Model):
    comment_id = models.IntegerField(unique=True)
    user_id = models.IntegerField()
    is_seen = models.IntegerField()
    content_type_id = models.IntegerField()
    object_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'minusstore_commentnotify'


class MinusstoreFiletype(models.Model):
    type_name = models.CharField(max_length=15)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    filetype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'minusstore_filetype'


class MinusstoreMinus(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'minusstore_minus'





class MinusstoreMinusauthorFiletypes(models.Model):
    minusauthor_id = models.IntegerField()
    filetype_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'minusstore_minusauthor_filetypes'


class MinusstoreMinuscategory(models.Model):
    name = models.CharField(max_length=15,default='null')
    display_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'minusstore_minuscategory'


class MinusstoreMinusplusrecord(models.Model):
    minus_id = models.IntegerField(unique=True, blank=True, null=True)
    user_id = models.IntegerField()
    file =  models.FileField(upload_to="static/files/pluses/")

    class Meta:
        managed = True
        db_table = 'minusstore_minusplusrecord'

class MinusstoreMinusauthor(models.Model):
    name = models.CharField(max_length=255,default='null')
    # minus = models.ManyToManyField(MinusstoreMinusrecord)
    class Meta:
        managed = True
        db_table = 'minusstore_minusauthor'
    def __str__(self):
        return self.name


class MinusstoreMinusrecord(models.Model):
    user = models.ForeignKey(User)
    file = models.FileField("Мінусовка",upload_to="static/files/minuses/",null=True,blank=True)
    title = models.CharField("Назва мінусовки",max_length=255)
    is_folk = models.IntegerField()
    author = models.ForeignKey(MinusstoreMinusauthor,null=True)
    arrangeuathor = models.CharField(max_length=50, blank=True, null=True)
    annotation = models.TextField()
    thematics = models.CharField(max_length=30, blank=True, null=True)
    tempo = models.CharField(max_length=10)
    staff = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    is_childish = models.IntegerField(default=0)
    is_amateur = models.IntegerField(default=0)
    is_ritual = models.IntegerField(default=0)
    lyrics = models.TextField("Текст пісні")
    plusrecord = models.FileField(upload_to="static/files/pluses/", blank=True, null=True)
    pub_date = models.DateTimeField()
    length = models.TimeField()
    bitrate = models.IntegerField()
    filesize = models.IntegerField()
    embed_video = models.TextField(blank=True, null=True)
    type_id = models.IntegerField()
    rating_votes = models.IntegerField()
    rating_score = models.IntegerField()
    alternative = models.IntegerField()


    class Meta:
        managed = True
        db_table = 'minusstore_minusrecord'

    def __str__(self):
        return self.title



class MinusstoreMinusrecordCategories(models.Model):
    minusrecord = models.ForeignKey(MinusstoreMinusrecord)
    minuscategory = models.ForeignKey(MinusstoreMinuscategory)

    class Meta:
        managed = True
        db_table = 'minusstore_minusrecord_categories'
        unique_together = (('minusrecord', 'minuscategory'),)




class MinusstoreMinusstats(models.Model):
    date = models.DateField()
    rate = models.IntegerField()
    minus_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'minusstore_minusstats'


class MinusstoreMinusstopword(models.Model):
    word = models.CharField(max_length=30)
    blocked = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'minusstore_minusstopword'

class MinusstoreMinusweekstats(models.Model):
    rate = models.IntegerField()
    minus_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'minusstore_minusweekstats'
