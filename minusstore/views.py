from django.shortcuts import render
from minus.models import NewsNewsitem,AuthUser,DjangoComments,MinusstoreMinusauthor
from django.http import HttpResponse
from django.core import serializers
from main.forms import AuthForm
from minusstore.forms import AddMinusForm
# from minus.autentification import *


def minusstore_main(request):
	form = AuthForm(request.POST)
	# signin(request,form)
	author = MinusstoreMinusauthor.objects.all().order_by('name')[:20]

	return render(request, 'minusstore/index.html' , {

		'author' : author,
		'form' : form,
		
		})


def minusstore_minus(request):
		form = AuthForm(request.POST)

		# signin(request,form)
		minus = get_object_or_404(MinusstoreMinusrecord,pk=pk)
		author = get_object_or_404(MinusstoreMinusauthor,pk=minus.author_id)
		comments = DjangoComments.objects.filter(object_pk=minus.pk,content_type_id=17)
		minus_user = get_object_or_404(AuthUser,pk=minus.user_id)
		upload_minuses_from_user = MinusstoreMinusrecord.objects.filter(user_id=minus_user.id).count()
		return render(request, 'minusstore/minus.html' , {
		'minus' : minus,
		'author' : author,
		'comments' : comments,
		'minus_user':minus_user,
		'upload_minuses' : upload_minuses_from_user,

		})

def add_minus(request):
		form = AuthForm(request.POST)
		# signin(request,form)
		form_add_minus = AddMinusForm(request.POST)

		return render(request, 'minusstore/add_minus.html' , {
		"form":form,
		"form_add_minus" : form_add_minus,
		})