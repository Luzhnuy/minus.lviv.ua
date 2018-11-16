from django.conf.urls import url,include

from . import views

urlpatterns = [
	url(r'^$',views.main,name="main"),
	url(r'^news/(?P<pk>[0-9]+)/$', views.news_index,name="news_index"),
	url(r'^comments/(?P<pk>[0-9]+)/$', views.comments,name="comments"),
	url(r'^likedislike/(?P<user_id>[0-9]+)/(?P<object_id>[0-9]+)/(?P<content_type_id>[0-9]+)/(?P<likeordislike>[0-1]+)/$', views.likedislike, name="likedislike"),
]
