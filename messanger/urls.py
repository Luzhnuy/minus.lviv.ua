from django.conf.urls import url
from . import views, api_views

urlpatterns = [
	url(r'^$', views.messanger,name='messanger'),
	url(r'^api/message-list/$', api_views.ListMessages.as_view(), name="listMessages"),
]
