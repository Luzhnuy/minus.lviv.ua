from django.shortcuts import render
from minus.models import NewsNewsitem,AuthUser,DjangoComments,MinusstoreMinusauthor
from django.http import HttpResponse
from django.core import serializers
from main.forms import AuthForm, RegForm

def user_page(request):
	
	form = AuthForm()

	return render(request, 'user/index.html',{
		'form' : form,
		})

def registration_page(request):
	Reg_form = RegForm(request.POST)
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
		'form' : Reg_form,
	})