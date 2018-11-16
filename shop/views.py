from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from shop.models import BlurbsBlurb
from django.contrib.auth.models import User



def main_shop(request):
	good = BlurbsBlurb.objects.all().order_by('-id')[:18]

	
	return render(request, 'shop/index.html' , {
		'goods':good,

	})
def goods(request,pk):
	good = BlurbsBlurb.objects.get(pk=pk)

	return render(request, 'shop/goods.html' , {'good':good,})
