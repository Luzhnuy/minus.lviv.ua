from django.shortcuts import render
from minus.models import *


def user_page(request):
	
	return render(request,'user/index.html')
