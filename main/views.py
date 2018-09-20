from django.shortcuts import render
from minus.models import NewsNewsitem,Userprofile,DjangoComments
from django.http import HttpResponse
from django.core import serializers
from .forms import AuthForm
# from minus.autentification import *






# Create your views here.


def main(request):
	form = AuthForm()
	# signin(request,form)

	
	
	news = NewsNewsitem.objects.all().order_by('-id')
	for i in news:
		i.user = Userprofile.objects.get(user_id = i.user_id)
	
		 
	
	return render(request, 'main/index.html' , {
	
		'news' : news,
		'form' : form,
		
		})

	
def comments(request,pk):


	comments = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk)
	comments = serializers.serialize("json",comments)


	return HttpResponse(comments)



