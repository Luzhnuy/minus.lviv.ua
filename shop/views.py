from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from minus.models import BlurbsBlurb


def main_shop(request):
	good = BlurbsBlurb.objects.all().order_by('-id')
	for i in good:
		i.user = AuthUser.objects.get(pk = i.user_id)
	return render(request, 'shop/index.html' , {
		'goods':good,			
				
	})
