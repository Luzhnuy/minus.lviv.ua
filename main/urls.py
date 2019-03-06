from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns


from . import views

urlpatterns = [
	url(r'^$',views.main,name="main"),
	url(r'^news/(?P<pk>[0-9]+)/$', views.news_index,name="news_index"),
	url(r'^add-new/$',views.AddNewsView.as_view(),name="add_new"),
	url(r'^comments/(?P<pk>[0-9]+)/$', views.GetComments.as_view(),name="comments"),
	url(r'^likedislike/(?P<user_id>[0-9]+)/(?P<object_id>[0-9]+)/(?P<content_type_id>[0-9]+)/(?P<likeordislike>[0-1]+)/$', views.likedislike, name="likedislike"),
	url(r'^rules/$',views.rules,name="rules"),
]
urlpatterns = format_suffix_patterns(urlpatterns)