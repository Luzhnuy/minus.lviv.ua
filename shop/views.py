from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from shop.models import BlurbsBlurb
from user.models import Userprofile
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def main_shop(request):
	good = BlurbsBlurb.objects.all().order_by('-id')
	paginator = Paginator(good, 40)
	page = request.GET.get('page')
	try:
	    good = paginator.page(page)

	except PageNotAnInteger:
	    good = paginator.page(1)
	       # print('second')
	except EmptyPage:
	    good = paginator.page(paginator.num_pages)
	        #print('third')


	return render(request, 'shop/index.html' , {
		'goods':good,

	})
def goods(request,pk):
	good = BlurbsBlurb.objects.get(pk=pk)

	return render(request, 'shop/goods.html' , {'good':good,})



def gave_business_or_private(request,bool):
	#goods = []
	good = None
	if bool == '1':
		good = BlurbsBlurb.objects.filter(is_user_business=1)
		# for g in a_goods:
		# 	if g.user.userprofile.is_business==1:
		# 		goods.append(g)
		paginator = Paginator(good, 40)
		page = request.GET.get('page')
		try:
		    good = paginator.page(page)
		except PageNotAnInteger:
			good = paginator.page(1)
			       # print('second')
		except EmptyPage:
		    good = paginator.page(paginator.num_pages)
					        #print('third')

		return render(request, 'shop/index.html',{'goods':good,'z':True,})

	else:
		good = BlurbsBlurb.objects.filter(is_user_business=0)
		paginator = Paginator(good, 40)
		page = request.GET.get('page')
		try:
		    good = paginator.page(page)
		except PageNotAnInteger:
			good = paginator.page(1)
			       # print('second')
		except EmptyPage:
		    good = paginator.page(paginator.num_pages)
					        #print('third')		
		return render(request, 'shop/index.html',{'goods':good,'f':True,})
