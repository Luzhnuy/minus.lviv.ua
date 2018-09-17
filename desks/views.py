from django.shortcuts import render
from minus.models import NewsNewsitem,AuthUser,DjangoComments

from django.http import HttpResponse
from django.core import serializers
from main.forms import AuthForm


# Create your views here.

def desk_of_shame(request):
	form = AuthForm()
	news = NewsNewsitem.objects.all().order_by('-id')
	for i in news:
		i.user = AuthUser.objects.get(pk = i.user_id)
	
		 

	return render(request, 'desks/shame.html' , {
		'form' : form,

		})

def desk_or_respect(request):
	form = AuthForm()
	news = NewsNewsitem.objects.all().order_by('-id')
	for i in news:
		i.user = AuthUser.objects.get(pk = i.user_id)
	
		 

	return render(request, 'desks/respect.html' , {
		'form' : form,
		})

