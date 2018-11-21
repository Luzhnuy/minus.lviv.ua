from django.db import models
from django.contrib.auth.models import User
# from user.models import AuthUser



class NewsNewsitem(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    body = models.TextField()
    allow_comments = models.IntegerField()
    pub_date = models.DateTimeField()
    preview = models.TextField()
    # objects = models.Manager()
    # manage = NewsNewsitemManager()

    class Meta:
        managed = True
        db_table = 'news_newsitem'
