from django.shortcuts import render
from minus.models import NewsNewsitem
from minus.tops_functions import *
# Create your views here.


def main(request):

	news = NewsNewsitem.objects.all()
	
		 

	return render(request, 'main/index.html' , {
		'minus_top_all_time' : top_minus_per_all_time(), 
		'minus_top_week' : top_minus_per_week(),
		'top_users' : top_users(),
		})
