from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
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
