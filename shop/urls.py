from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$',views.main_shop,name='main_shop'),
]
