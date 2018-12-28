from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BlurbsBlurbcategory(models.Model):
    title = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'blurbs_blurbcategory'


    def __str__(self):
        return self.title


class BlurbsGeocity(models.Model):
    title = models.CharField(max_length=30)
    region_id = models.IntegerField()
    is_city = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'blurbs_geocity'


class BlurbsGeoregion(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'blurbs_georegion'

    def __str__(self):
        return self.title

class BlurbsBlurb(models.Model):
    title = models.CharField('Назва',max_length=120)
    description = models.TextField('Опис товару')
    buysell = models.CharField('Ціна',max_length=255)
    user = models.ForeignKey(User,on_delete="CASCADE")
    category = models.ForeignKey(BlurbsBlurbcategory,on_delete="PROTECT")
    pub_date = models.DateTimeField(auto_now_add=True)
    georegion = models.ForeignKey(BlurbsGeoregion,on_delete="PROTECT")
    is_user_business = models.BooleanField(default=0)
    class Meta:
        managed = True
        db_table = 'blurbs_blurb'
        # fields = '__all__'

    def __str__(self):
        return self.title
