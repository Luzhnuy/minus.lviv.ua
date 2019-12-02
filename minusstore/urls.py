from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from . import views

urlpatterns = [
  	url(r'^$',views.minusstore_main, name="minusstore_main"),
    url(r'^minus-filter$',views.minusstore_filter , name="minusstore_filter"),
  	url(r'^minus/(?P<pk>[0-9]+)/$',views.minusstore_minus, name="minus"),
  	url(r'^add_minus/',views.add_minus, name="add_minus"),
  	url(r'^if-minus-correct/(?P<pk>[0-9]+)/$',views.if_minus_correct, name="if_minus_correct"),
  	url(r'^generete_pdf/(?P<pk>[0-9]+)/$',views.pdf_generete, name="generete_pdf"),
  	url(r'^letters-filter/(?P<letter>[a-zA-Z0-9А-ЯЄІ]+)/$',views.letters_filter, name="letter_filter"),
    url(r'^give/(?P<author_id>[0-9]+)/$', views.gave, name="gave_minus"),
    url(r'^subscribe/', views.subscribe, name="subscribe"),
    url(r'^minus-archiv/(?P<day>[0-9]+)/$', views.archiv_of_minuses, name="archiv_of_minuses"),
    url(r'^minus-search/$',views.minus_search,name="minus-search"),
    url(r'^get_authors/(?P<letter>[a-zA-Z0-9А-ЯЄІ]+)/$', views.MinusAuthor.as_view(), name="get_minus_author"),
	url(r'all-minuses-by-date/$', views.all_minuses_by_date, name="all-minuses-by-date"),
    url(r'minus-update/(?P<pk>[0-9]+)/$',views.MinusRecordUpdate.as_view(),name="minus-update"),
    url(r'minus-arrangement-assessment/(?P<user_id>[0-9]+)/(?P<minus_id>[0-9]+)/(?P<assessment>[0-9]+)/$', views.minusarrangement, name="minus_arrangement"),
    url(r'minus-quality-assessment/(?P<user_id>[0-9]+)/(?P<minus_id>[0-9]+)/(?P<assessment>[0-9]+)/$', views.minusquality, name="minus_quality"),

]


urlpatterns = format_suffix_patterns(urlpatterns)
