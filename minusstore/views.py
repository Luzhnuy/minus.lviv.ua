from django.shortcuts import render
from minus.models import NewsNewsitem,AuthUser,DjangoComments,MinusstoreMinusauthor
from django.http import HttpResponse
from django.core import serializers
from main.forms import AuthForm
from minusstore.forms import AddMinusForm
from minus.autentification import *


def minusstore_main(request):
	form = AuthForm(request.POST)
	signin(request,form)
	author = MinusstoreMinusauthor.objects.all().order_by('name')[:20]

	return render(request, 'minusstore/index.html' , {

		'author' : author,
		'form' : form,
		
		})


def minusstore_minus(request):
		form = AuthForm(request.POST)
		signin(request,form)


		return render(request, 'minusstore/minus.html' , {
		'usr' : request.session['usr'],
		})

def add_minus(request):
		form = AuthForm(request.POST)
		signin(request,form)
		form_add_minus = AddMinusForm(request.POST)

		return render(request, 'minusstore/add_minus.html' , {
		'usr' : request.session['usr'],
		"form_add_minus" : form_add_minus,
		})