from django import forms
from minus.models import AuthUser


class AuthForm(forms.ModelForm):

	class Meta:
		model = AuthUser
		fields = ('email', 'password', )



class RegForm(forms.ModelForm):		

	class Meta:
		model = AuthUser
		fields = ('email', 'username', 'first_name', 'last_name', 'password',)