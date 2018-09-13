from django.shortcuts import render
from minus.models import NewsNewsitem,AuthUser,DjangoComments,MinusstoreMinusauthor
from minus.tops_functions import *
from django.http import HttpResponse
from django.core import serializers
from main.forms import AuthForm
from minusstore.forms import AddMinusForm
from minus.autentification import *
from minus.new_minuses import *

def minusstore_main(request):
	form = AuthForm(request.POST)
	signin(request,form)
	author = MinusstoreMinusauthor.objects.all().order_by('name')[:20]

	return render(request, 'minusstore/index.html' , {
		'minus_top_all_time' : top_minus_per_all_time(), 
		'minus_top_week' : top_minus_per_week(),
		'top_users' : top_users(),
		'author' : author,
		'forum' : last_forum(),
		'form' : form,
		'new_m':new_minuses(),
		})


def minusstore_minus(request):
		form = AuthForm(request.POST)
		signin(request,form)


		return render(request, 'minusstore/minus.html' , {
		'minus_top_all_time' : top_minus_per_all_time(), 
		'minus_top_week' : top_minus_per_week(),
		'top_users' : top_users(),
		'forum' : last_forum(),
		'usr' : request.session['usr'],
		'new_m':new_minuses(),
		})

def add_minus(request):
		form = AuthForm(request.POST)
		signin(request,form)
		form_add_minus = AddMinusForm(request.POST)

		return render(request, 'minusstore/add_minus.html' , {
		'minus_top_all_time' : top_minus_per_all_time(), 
		'minus_top_week' : top_minus_per_week(),
		'top_users' : top_users(),
		'forum' : last_forum(),
		'usr' : request.session['usr'],
		'new_m':new_minuses(),
		"form_add_minus" : form_add_minus,
		})