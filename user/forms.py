from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from main.models import ModeratorMessages
from album.models import PhotosPhotoalbum, PhotosPhoto
from .models import UserPost,Userprofile
from django.shortcuts import render
import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse,HttpResponseRedirect


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)


    class Meta:
        model = User
        fields = ("username", "first_name","last_name","email","password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        print('G')
        user.is_active = 0
        user.email = self.cleaned_data["email"]
        print('Z')
        user.last_login = datetime.datetime.now()
        print('F')
        if commit:
            print('Q')
            user.save()
        print('W')
        return user



class AddUserPost(forms.ModelForm):

    class Meta:
        model = UserPost
        fields = ('text','image')

    def save(self,request,commit=True):
        post = super(AddUserPost,self).save(commit=False)
        post.userprofile = Userprofile.objects.get(user_id = request.user.id)
        if commit:
            post.save()

        return post




class EmailAuthenticationForm(AuthenticationForm):
    def clean_username(self):
        username = self.data['username']
        if '@' in username:
            try:
                username = User.objects.get(email=username)
                username.last_login = datetime.datetime.now()
            except User.DoesNotExist:
                return HttpResponseRedirect('false_auth')
        else:
            try:
                username = User.objects.get(username=username)
                username.last_login = datetime.datetime.now()
            except User.DoesNotExist:
                return HttpResponseRedirect('false_auth')

        return username

class AddModeratorMessagesForm(forms.ModelForm):
    class Meta:
        model = ModeratorMessages
        fields = ('attention_message',)

    def save(self,request,content_type_id,object_pk,commit=True):
        post = super(AddModeratorMessagesForm,self).save(commit=False)
        post.user = request.user
        post.content_id = content_type_id
        post.object_pk = object_pk
        if commit:
            print("add moderator messages form presave")
            post.save()
            print("add moderator messages form save")

        return post

class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = PhotosPhoto
        fields = ('title','image',)
