from django.shortcuts import render
from minus.models import DjangoComments
from user.models import Userprofile
from django.http import HttpResponse
from django.core import serializers
from main.forms import AuthForm
import datetime


# Create your views here.

def desk_of_shame(request):
	banned_users = []
	users = Userprofile.objects.filter(banned=1)
	for u in users:
		if u.banned_until>datetime.date.today():
			banned_users.append(u)
	return render(request, 'desks/shame.html' , {
		"users":banned_users,

	})

def desk_or_respect(request):
	banned_users = []
	users = Userprofile.objects.filter(banned=1)
	for u in users:
		if u.banned_until>datetime.date.today():
			banned_users.append(u)
	return render(request, 'desks/respect.html' , {
		"users":banned_users,

	})
