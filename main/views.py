from django.shortcuts import render,get_object_or_404
from minus.models import DjangoComments,Likedislike
from main.models import NewsNewsitem
from django.contrib.auth.models import User
from user.models import Userprofile
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
import json
from .forms import AuthForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from minus.autentification import *






# Create your views here.


def main(request):

	# signin(request,form)



	news_objects = NewsNewsitem.objects.all().order_by('-id')
	# comments_count = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk).count()

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
	count =   DjangoComments.objects.filter(content_type_id = 51,object_pk = pk).count()
	return render(request, 'main/news.html' , {
		'count': count,


		'news' : new,


	})

def comments(request,pk):


	comments = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk)

	comments = serializers.serialize("json",comments)


	return HttpResponse(comments)


def likedislike(request, user_id, object_id, content_type_id,likeordislike):
	try:
		likeorodislike = Likedislike.objects.get(object_id=object_id,type_id=content_type_id,user_id=user_id)
		print(likeorodislike.likes)

		if likeordislike == '1' and likeorodislike.likes==False:
			likeorodislike.likes = 1
			likeorodislike.save()
			try:
				likes = Likedislike.objects.filter(type_id= content_type_id,object_id=object_id,likes=1).count()
			except:
				likes=0
			dislikes =  Likedislike.objects.filter(type_id= content_type_id,object_id=object_id,likes=0).count()
			likeanddislike = json.dumps({'likes':likes,'dislikes':dislikes})
			return HttpResponse(likeanddislike)
		elif likeordislike == '0' and likeorodislike.likes==True:
			likeorodislike.likes = 0
			likeorodislike.save()
			likes = Likedislike.objects.filter(type_id= content_type_id,object_id=object_id,likes=1).count()
			dislikes =  Likedislike.objects.filter(type_id= content_type_id,object_id=object_id,likes=0).count()
			likeanddislike = json.dumps({'likes':likes,'dislikes':dislikes})
			return HttpResponse(likeanddislike)
		else:
			return HttpResponse('figovo')

		#return HttpResponse(likeanddislike)
	except Likedislike.DoesNotExist:
		print('zbs')
		likedislike = Likedislike.objects.create(user_id = user_id,object_id = object_id, type_id = content_type_id, likes = likeordislike )
		likedislike.save()
		likes = Likedislike.objects.filter(type_id= content_type_id,object_id=object_id,likes=1).count()
		dislikes =  Likedislike.objects.filter(type_id= content_type_id,object_id=object_id,likes=0).count()
		# likes = serializers.serialize('json',likes)
		# dislikes = serializers.serialize('json',dislikes)
		print(likes)
		print(dislikes)
		print('zbc2')
		likeanddislike = {'likes':likes,'dislikes':dislikes}
		print('zbc3')
		likeanddislike = json.dumps(likeanddislike)
		print('zbc4')
		return HttpResponse(likeanddislike)
