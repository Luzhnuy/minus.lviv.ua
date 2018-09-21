from django.shortcuts import render,get_object_or_404
from minus.models import NewsNewsitem,AuthUser,DjangoComments,MinusstoreMinusauthor,MinusstoreMinusrecord,MinusstoreMinusrecordCategories,MinusstoreMinuscategory
from django.http import HttpResponse
from django.core import serializers
from main.forms import AuthForm
from minusstore.forms import AddMinusForm
# from minus.autentification import *


def minusstore_main(request):
	form = AuthForm(request.POST)
	# signin(request,form)
	author = MinusstoreMinusauthor.objects.all().order_by('name')[:20]
	for i in author:
		i.minus = MinusstoreMinusrecord.objects.filter(author_id=i.pk)

	return render(request, 'minusstore/index.html' , {

		'author' : author,
		'form' : form,
		
		})


def minusstore_minus(request,pk):
		form = AuthForm(request.POST)
		# signin(request,form)
		minus = get_object_or_404(MinusstoreMinusrecord,pk=pk)
		author = get_object_or_404(MinusstoreMinusauthor,pk=minus.author_id)
		comments = DjangoComments.objects.filter(object_pk=minus.pk,content_type_id=17)
		minus_user = get_object_or_404(AuthUser,pk=minus.user_id)
		upload_minuses_from_user = MinusstoreMinusrecord.objects.filter(user_id=minus_user.id).count()
		minus.filesize = int(minus.filesize/1000000)
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

def if_minus_correct(request,pk):
		form = AuthForm(request.POST)
		minus = MinusstoreMinusrecord.objects.get(pk=pk)
		category_id = MinusstoreMinusrecordCategories.objects.get(minusrecord_id=minus.pk)
		сategory_id = category_id.minuscategory_id
		
		# category = MinusstoreMinuscategory.objects.get(pk=category_id)
		
		return render(request, 'minusstore/look_on_minus_correct.html' , {
		"form":form,
		'minus':minus,
		# 'category':category,
		
		})
