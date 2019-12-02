from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'user-album/(?P<pk>[0-9]+)/$',views.user_album,name="user_album"),
]