from django.shortcuts import render,get_object_or_404
from minus.models import NewsNewsitem,Userprofile,DjangoComments,AuthUser
from django.http import HttpResponse
from django.core import serializers
from .forms import AuthForm
# from minus.autentification import *






# Create your views here.


def main(request):

	# signin(request,form)

	
	
	news = NewsNewsitem.objects.all().order_by('-id')
	for i in news:
		i.user = AuthUser.objects.get(pk = i.user_id)
	
		 
	
	return render(request, 'main/index.html' , {
	
		'news' : news,
		
		
		})


def news_index(request,pk):
	



	new = get_object_or_404(NewsNewsitem,pk=pk)

	new.user = AuthUser.objects.get(pk = new.user_id)
	new.comments = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk)
	for i in new.comments:
		i.user = AuthUser.objects.get(pk = i.user_id)

	return render(request, 'main/news.html' , {
	
		'news' : new,
	
		
		})	
	
def comments(request,pk):


	comments = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk)
	comments = serializers.serialize("json",comments)


	return HttpResponse(comments)



