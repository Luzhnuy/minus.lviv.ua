from django.db import models
from django.contrib.auth.models import User
# from user.models import AuthUser



class NewsNewsitem(models.Model):
    user = models.ForeignKey(User,blank=True, null=True,on_delete=models.SET_NULL)
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



class ModeratorMessages(models.Model):
    attention_message = models.CharField(max_length=500)
    user = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL)
    content_id = models.IntegerField()
    object_pk = models.IntegerField()

    class Meta:
        db_table = "moderator_messages"
        managed = True


    def __str__(self):
        return self.attention_message
