from main.forms import AuthForm
from minus.models import AuthUser
from django.shortcuts import render

def signin(request,form):
	auth = AuthUser.objects.all()
	
	if request.method == "POST" and form.is_valid():
		for u in auth:
			if form.cleaned_data.get('email') == u.email and form.cleaned_data.get('password') == u.password:
				return u
				
					
		