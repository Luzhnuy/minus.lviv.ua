from django.shortcuts import render
from minus.models import NewsNewsitem,AuthUser,DjangoComments
from minus.tops_functions import *
from django.http import HttpResponse
from django.core import serializers



# Create your views here.


def main(request):

	news = NewsNewsitem.objects.all().order_by('-id')
	for i in news:
		i.user = AuthUser.objects.get(pk = i.user_id)
	
		 

	return render(request, 'main/index.html' , {
		'minus_top_all_time' : top_minus_per_all_time(), 
		'minus_top_week' : top_minus_per_week(),
		'top_users' : top_users(),
		'news' : news,
		})


def comments(request,pk):


	comments = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk)
	comments = serializers.serialize("json",comments)


	return HttpResponse(comments)