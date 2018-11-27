from django.db import models
from django.contrib.auth.models import User


class BlurbsBlurb(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    buysell = models.CharField(max_length=1)
    user = models.ForeignKey(User)
    category_id = models.IntegerField()
    pub_date = models.DateTimeField()
    georegion_id = models.IntegerField(blank=True, null=True)
    geocity_id = models.IntegerField(blank=True, null=True)
    is_user_business = models.BooleanField(default=0)
    class Meta:
        managed = True
        db_table = 'blurbs_blurb'


class BlurbsBlurbcategory(models.Model):
    title = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'blurbs_blurbcategory'


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
