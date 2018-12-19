from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.messanger,name='messanger'),
	url(r'^(?P<pk>[0-9]+)/$',views.messages, name="message_user"),
]
