from django.shortcuts import render
from minus.models import NewsNewsitem,AuthUser,DjangoComments
from minus.tops_functions import *
from django.http import HttpResponse
from django.core import serializers
from main.forms import AuthForm
from minus.new_minuses import *

# Create your views here.

def desk_of_shame(request):
	form = AuthForm()
	news = NewsNewsitem.objects.all().order_by('-id')
	for i in news:
		i.user = AuthUser.objects.get(pk = i.user_id)
	
		 

	return render(request, 'desks/shame.html' , {
		'minus_top_all_time' : top_minus_per_all_time(), 
		'minus_top_week' : top_minus_per_week(),
		'top_users' : top_users(),
		'news' : news,
		'forum' : last_forum(),
		'form' : form,
		'new_m':new_minuses(),
		})

def desk_or_respect(request):
	form = AuthForm()
	news = NewsNewsitem.objects.all().order_by('-id')
	for i in news:
		i.user = AuthUser.objects.get(pk = i.user_id)
	
		 

	return render(request, 'desks/respect.html' , {
		'minus_top_all_time' : top_minus_per_all_time(), 
		'minus_top_week' : top_minus_per_week(),
		'top_users' : top_users(),
		'news' : news,
		'forum' : last_forum(),
		'form' : form,
		'new_m':new_minuses(),
		})

