from django.shortcuts import render
from minus.models import MinusstoreMinusstats, MinusstoreMinusrecord
from minus.tops_functions import *
# Create your views here.


def main(request):

	
		 

	return render(request, 'main/index.html' , {'minus_top_all_time' : top_minus_per_all_time() })
