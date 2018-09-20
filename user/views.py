from django.shortcuts import render
from minus.models import NewsNewsitem,AuthUser,DjangoComments,MinusstoreMinusauthor
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from main.forms import AuthForm, RegForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.models import User


def user_page(request):
	
	form = AuthForm()

	return render(request, 'user/index.html',{
		'form' : form,
		})


def registration_page(request):
	Reg_form = RegForm(request.POST)
	form = AuthForm(request.POST)
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
		'Reg_form' : Reg_form,
	})



def signin(request):
	form = AuthForm(request.POST)
	
	if request.method == "POST":
		if form.is_valid():
			login = request.POST['email']
			pas = request.POST['password']
			user = authenticate(email=login, password=pas)
			if user is not None:
				login(request,user)
				
				return render(request, 'main/index.html' , {
					'user' : user,
					})
			else:
				
				return render(request, 'user/registration.html' , {})
	else:
			return HttpResponse(len(User.objects.all()))		