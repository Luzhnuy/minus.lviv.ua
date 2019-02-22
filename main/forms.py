from django import forms
# from user.models import AuthUser
from django.contrib.auth.models import User
from main.models import NewsNewsitem

class AuthForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'password', )




class AddNews(forms.ModelForm):
	class Meta:
		model = NewsNewsitem
		fields = ('title','preview','body','img','allow_comments')

