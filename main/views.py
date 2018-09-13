from django.shortcuts import render
from minus.models import NewsNewsitem,AuthUser,DjangoComments
from minus.tops_functions import *
from django.http import HttpResponse
from django.core import serializers
from .forms import AuthForm
from minus.autentification import *
from minus.new_minuses import *



# Create your views here.


def main(request):
	form = AuthForm()
	request.session['usr']=signin(request,form)
	news = NewsNewsitem.objects.all().order_by('-id')
	for i in news:
		i.user = AuthUser.objects.get(pk = i.user_id)
	
		 
	usr = request.session['usr']
	return render(request, 'main/index.html' , {
		'minus_top_all_time' : top_minus_per_all_time(), 
		'minus_top_week' : top_minus_per_week(),
		'top_users' : top_users(),
		'news' : news,
		'forum' : last_forum(),
		'form' : form,
		'usr' : usr,
		'new_m':new_minuses(),
		})


def comments(request,pk):


	comments = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk)
	comments = serializers.serialize("json",comments)


	return HttpResponse(comments)



