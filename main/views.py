from django.shortcuts import render,get_object_or_404
from minus.models import DjangoComments,Likedislike
from main.models import NewsNewsitem
from django.contrib.auth.models import User
from user.models import Userprofile
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from .forms import AuthForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from minus.autentification import *






# Create your views here.


def main(request):

	# signin(request,form)



	news_objects = NewsNewsitem.objects.all().order_by('-id')

	paginator = Paginator(news_objects, 10)
	page = request.GET.get('page')
	try:

		news = paginator.page(page)
		print('first')
	except PageNotAnInteger:
		news = paginator.page(1)
		print('second')
	except EmptyPage:
		news = paginator.page(paginator.num_pages)
		print('third')

	for new in news:
		new.comments_count = DjangoComments.objects.filter(content_type_id=51,object_pk=new.id).count()


	return render(request, 'main/index.html' , {

		'news' : news,


	})



def news_index(request,pk):




	new = get_object_or_404(NewsNewsitem,pk=pk)

	# new.user = User.objects.get(pk = new.user_id)
	new.comments = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk)

	return render(request, 'main/news.html' , {



		'news' : new,


	})

def comments(request,pk):


	comments = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk)
	comments = serializers.serialize("json",comments)


	return HttpResponse(comments)


def likedislike(request, user_id, object_id, content_type_id,likeordislike):
	try:
		likeanddislike = Likedislike.objects.get(content_type_id= 17,object_id = object_id)
		print(likeanddislike.likes)
		if likeordislike=='1':
			likeanddislike.likes=likeanddislike.likes+1
			print(likeanddislike.likes)
			likeanddislike.save()
		else:
			likeanddislike.dislikes=likeanddislike.dislikes+1
			print(likeanddislike.dislikes)
			likeanddislike.save()
		likeanddislike=serializers.serialize("json",likeanddislike)
		return HttpResponse(likeanddislike);
	except Likedislike.DoesNotExist:
		print("ERORROROROROROROROOROROROOROROROROROROORORORROORORORORORORrororororoo")
		likeanddislike=0
		if likeordislike=='1':
	 		Likedislike(user_id=user_id,object_id=object_id,content_type_id=content_type_id,likes = likeanddislike+1,dislikes=likeanddislike)
		else:
	 		Likedislike(user_id=user_id,object_id=object_id,content_type_id=content_type_id,likes=likeanddislike,dislikes=likeanddislike+1)
		# likeanddislike=serializers.serialize("json",likeanddislike)
		return HttpResponse(likeanddislike);
