from django.shortcuts import render
from minus.models import *


def user_page(request):
	user = AlbumsAudio.object.get()
	return render(request,'user/index.html',{'user' : user})
