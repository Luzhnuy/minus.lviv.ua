from django import forms
# from user.models import AuthUser
from django.contrib.auth.models import User
from main.models import NewsNewsitem
from minus.models import DjangoComments

class AuthForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'password', )




class AddNews(forms.ModelForm):
	class Meta:
		model = NewsNewsitem
		fields = ('title','preview','body','img','allow_comments')


class AddComments(forms.ModelForm):

	class Meta:
		model = DjangoComments
		fields = ('comment',)

	def save(self, pk, request, content_type_id, commit=True):
		comment = super(AddComments, self).save(commit=False)
		comment.content_type_id = content_type_id
		comment.object_pk = pk
		comment.user = request.user
		comment.user_name = request.user.username
		comment.user_email = request.user.email
		comment.site_id = pk
		comment.user_url = '/user/user/' + str(request.user.id) + '/'
		comment.is_public = 1
		comment.is_removed = 0
		if commit:
			comment.save()
		return comment	
