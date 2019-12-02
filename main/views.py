from django.shortcuts import render,get_object_or_404
from minus.models import DjangoComments,Likedislike
from album.models import PhotosPhotoalbum,PhotosPhoto
from main.models import NewsNewsitem
from shop.models import BlurbsBlurb
from minusstore.models import MinusstoreMinusrecord
from django.contrib.auth.models import User
from user.models import Userprofile,UserActivitys,SubscribeOnComments
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import FormView
from django.core import serializers
from .forms import AuthForm,AddNews,AddComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# from minus.autentification import *
import json






def main(request):
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



def rules(request):

	return render(request,'main/rules.html',{})



def news_index(request,pk):
	new = get_object_or_404(NewsNewsitem,pk=pk)
	new.comments = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk)
	count = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk).count()
	for c in new.comments:
		c.answer = DjangoComments.objects.filter(object_pk = c.id, content_type_id = 45)
		c.likes = Likedislike.objects.filter(type_id= 45,object_id = c.pk,likes=1).count()
		c.dislikes = Likedislike.objects.filter(type_id= 45,object_id = c.pk,likes=0).count()
	# for n_c in new.comments:
		# n_c.photo = PhotosPhotoalbum.objects.get(content_type_id = 20,user_id = n_c.user.id)
		# n_c.photo = PhotosPhoto.objects.filter(album_id = n_c.photo.id)[0]
	add_comment_form = AddComments(request.POST)
	if request.user.is_authenticated:
		if request.method == "POST":
			if add_comment_form.is_valid():
				comment = add_comment_form.cleaned_data['comment']
				if comment[0] == "@":
					print(comment)
					comment = comment.split(" ")
					user = comment[0]
					comment_id = user.split('#')
					comment_id = comment_id[1]
					print(user)
					print(comment_id)
					comment = user[0]
					add_comment = add_comment_form.save(commit=True,pk=comment_id,request=request,content_type_id=45)
				else:
					add_comment = add_comment_form.save(commit=True,pk=pk,request=request,content_type_id=51)
				if request.POST.get('subscribe'):
					for subscriber in SubscribeOnComments.objects.filter(content_type_id = 51, object_pk = pk):
						UserActivitys.objects.create(from_user = request.user,type='s',to_user_id = subscriber.user.id,activity_to=pk)
					try:
						SubscribeOnComments.objects.get(content_type_id = 51,object_pk = pk, user = request.user)
					except SubscribeOnComments.DoesNotExist:
						SubscribeOnComments.objects.create(
							content_type_id=51,
							object_pk = pk,
							user = request.user
						)
					return render(request, 'minusstore/minus.html' , {
                    'likes' : likes,
                    'dislikes' : dislikes,
                    'minus' : minus,
                    'author' : author,
                    'minus_user':minus_user,
                    'upload_minuses' : upload_minuses_from_user,
                    'add_comment_form':add_comment_form,
                })
	return render(request, 'main/news.html', dict(count=count, news=new,add_comment_form=add_comment_form))




class AddNewsView(FormView):
	form_class= AddNews
	template_name = "main/add_news.html"
	success_url = '/'

	def form_valid(self,form):
		print('add news valid')
		form.instance.user = self.request.user
		form_data = form.save()
		return super().form_valid(form)







# def comments(request,pk):


# 	comments = DjangoComments.objects.filter(content_type_id = 51,object_pk = pk)

# 	comments = serializers.serialize("json",comments)


# 	return HttpResponse(comments)

class GetComments(APIView):

	def get_objects(self,pk):
		try:
			return DjangoComments.objects.filter(content_type_id = 51,object_pk = pk)
		except DjangoComments.DoesNotExist:
			raise Http404



	def get(self,request,pk,format=None):
		comments = self.get_objects(pk = pk)
		serializer_context = {
            'request': request,
        }
		comments = CommentSerializer(comments,many=True,	context=serializer_context)
		return Response(comments.data)



def likedislike(request, user_id, object_id, content_type_id,likeordislike):
	try:
		likeorodislike = Likedislike.objects.get(object_id=object_id,type_id=content_type_id,user_id=user_id)
		print(likeorodislike.likes)
		user = User.objects.get(pk=user_id)
		if content_type_id == '17':
			minus = MinusstoreMinusrecord.objects.get(pk = object_id)
		elif content_type_id == '52':
			minus = BlurbsBlurb.objects.get(pk = object_id)
		elif content_type_id == '45':
			minus = DjangoComments.objects.get(pk = object_id)
		print(minus)
		print("----------------------------------------")
		print(likeorodislike.likes == True)
		print(likeordislike)
		if likeordislike == '1' and likeorodislike.likes==False:
			likeorodislike.likes = 1
			likeorodislike.save()
			print('save')
			try:
				likes = Likedislike.objects.filter(type_id= content_type_id,object_id=object_id,likes=1).count()
			except:
				likes=0
			dislikes =  Likedislike.objects.filter(type_id= content_type_id,object_id=object_id,likes=0).count()
			likeanddislike = json.dumps({'likes':likes,'dislikes':dislikes})
			UserActivitys.objects.filter(from_user=user,to_user_id=minus.user.id,type='d',activity_to = object_id).update(type='l')
			return HttpResponse(likeanddislike)
		elif likeordislike == '0' and likeorodislike.likes==True:
			likeorodislike.likes = 0
			likeorodislike.save()
			likes = Likedislike.objects.filter(type_id= content_type_id,object_id=object_id,likes=1).count()
			UserActivitys.objects.filter(from_user=user,to_user_id=minus.user.id,type='l',activity_to = object_id).update(type='d')
			dislikes =  Likedislike.objects.filter(type_id= content_type_id,object_id=object_id,likes=0).count()
			likeanddislike = json.dumps({'likes':likes,'dislikes':dislikes})
			return HttpResponse(likeanddislike)
		else:
			return HttpResponse('figovo')

		#return HttpResponse(likeanddislike)
	except Likedislike.DoesNotExist:
		print('zbs')
		likedislike = Likedislike.objects.create(user_id = user_id,object_id = object_id, type_id = content_type_id, likes = likeordislike )
		if content_type_id == '17':
			minus = MinusstoreMinusrecord.objects.get(pk = object_id)
		elif content_type_id == '52':
			minus = BlurbsBlurb.objects.get(pk = object_id)
		elif content_type_id == '45':
			minus = DjangoComments.objects.get(pk = object_id)
		print(minus)
		user = User.objects.get(pk=user_id)
		if likeordislike== '1':
			UserActivitys.objects.create(from_user=user,to_user_id=minus.user.id,type='l',activity_to = object_id)
		else:
			UserActivitys.objects.create(from_user=user,to_user_id=minus.user.id,type='d',activity_to = object_id)
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
