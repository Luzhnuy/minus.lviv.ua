from django.shortcuts import render
from minus.tops_functions import *
from django.http import HttpResponse
from django.core import serializers

def main_shop(request):
	
	return render(request, 'shop/index.html' , {
		# 'minus_top_all_time' : top_minus_per_all_time(), 
		# 'minus_top_week' : top_minus_per_week(),
		# 'top_users' : top_users(),
				})
