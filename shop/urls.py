from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$',views.main_shop,name='main_shop'),
	url(r'^goods/(?P<pk>[0-9]+)/$',views.goods,name='goods'),
	url(r'^is_business/(?P<bool>[0-1]+)/$',views.gave_business_or_private,name='is_business'),
	url(r'^add_good',views.add_blurb,name="add_blurb"),
]
