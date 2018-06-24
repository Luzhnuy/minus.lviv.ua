from django.shortcuts import render
from minus.models import NewsNewsitem,AuthUser,DjangoComments
from minus.tops_functions import *
from django.http import HttpResponse
from django.core import serializers

# Create your views here.


def minusstore_main(request):

	return render(request, 'minusstore/index.html' , {
		'minus_top_all_time' : top_minus_per_all_time(), 
		'minus_top_week' : top_minus_per_week(),
		'top_users' : top_users(),
		
		})

