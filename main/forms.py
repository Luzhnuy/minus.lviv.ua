from django import forms
from minus.models import AuthUser
from django.contrib.auth.models import User

class AuthForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('email', 'password', )



class RegForm(forms.ModelForm):		

	class Meta:
		model = User
		fields = ('email', 'username', 'first_name', 'last_name', 'password',)