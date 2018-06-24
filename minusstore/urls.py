from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
  	
  	url(r'^$',views.minusstore_main, name="minusstore_main"),

]