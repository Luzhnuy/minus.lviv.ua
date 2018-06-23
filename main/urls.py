from django.conf.urls import url,include

from . import views

urlpatterns = [
	url(r'^$',views.main,name="main"),
	url(r'^comments/(?P<pk>[0-9]+)/$', views.comments,name="comments")
]
