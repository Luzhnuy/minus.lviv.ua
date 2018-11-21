from django.shortcuts import render
from minus.models import DjangoComments

from django.http import HttpResponse
from django.core import serializers
from main.forms import AuthForm


# Create your views here.

def desk_of_shame(request):

	return render(request, 'desks/shame.html' , {


	})

def desk_or_respect(request):

	return render(request, 'desks/respect.html' , {

		})
