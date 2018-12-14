from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
  	url(r'^$',views.minusstore_main, name="minusstore_main"),
  	url(r'^minus/(?P<pk>[0-9]+)/$',views.minusstore_minus, name="minus"),
  	url(r'^add_minus/',views.add_minus, name="add_minus"),
  	url(r'^if-minus-correct/(?P<pk>[0-9]+)/$',views.if_minus_correct, name="if_minus_correct"),
  	url(r'^generete_pdf/(?P<pk>[0-9]+)/$',views.pdf_generete, name="generete_pdf"),
  	url(r'^letters-filter/(?P<letter>[a-zA-Z0-9А-ЯЄІ]+)/$',views.letters_filter, name="letter_filter"),
    url(r'^give/(?P<author_id>[0-9]+)/$', views.gave, name="gave_minus"),
    url(r'^subscribe/', views.subscribe, name="subscribe"),

]
