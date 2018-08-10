from django.shortcuts import render
from minus.models import NewsNewsitem,AuthUser,DjangoComments,MinusstoreMinusauthor
from minus.tops_functions import *
from django.http import HttpResponse
from django.core import serializers
from main.forms import AuthForm, RegForm

def user_page(request):
	
	form = AuthForm()

	return render(request, 'user/index.html',{
		'minus_top_all_time' : top_minus_per_all_time(), 
		'minus_top_week' : top_minus_per_week(),
		'top_users' : top_users(),
		'form' : form,
		'forum' : last_forum(),
		})

def registration_page(request):
	Reg_form = RegForm()
	if request.method == "POST":
		if Reg_form.is_valid():
			user = Reg_form.save(commit=False)
			user.email = request.email
			user.username = request.username 
			user.first_name = request.first_name
			user.last_name = request.last_name
			user.password = request.password
			user.save()
			

		
	return render(request, 'user/registration.html',{
		'minus_top_all_time' : top_minus_per_all_time(), 
		'minus_top_week' : top_minus_per_week(),
		'top_users' : top_users(),
		'form' : Reg_form,
		'forum' : last_forum(),
	})