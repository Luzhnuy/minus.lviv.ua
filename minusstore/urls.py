from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
  	
  	url(r'^$',views.minusstore_main, name="minusstore_main"),
  	url(r'minus/(?P<pk>[0-9]+)/$',views.minusstore_minus, name="minus"),
  	url(r'add_minus/',views.add_minus, name="add_minus"),

]