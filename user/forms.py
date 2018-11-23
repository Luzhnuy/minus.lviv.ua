from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime
from django.contrib.auth.forms import AuthenticationForm


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)


    class Meta:
        model = User
        fields = ("username", "first_name","last_name","email","password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.last_login = datetime.datetime.now()
        if commit:
            user.save()
        return user


class EmailAuthenticationForm(AuthenticationForm):
    def clean_username(self):
        username = self.data['username']
        if '@' in username:
            try:
                username = User.objects.get(email=username)
                username.last_login = datetime.datetime.now()
            except User.DoesNotExist:
                raise ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username':self.username_field.verbose_name},
                )
        else:
            try:
                username = User.objects.get(username=username)
                username.last_login = datetime.datetime.now()
            except User.DoesNotExist:
                raise ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username':self.username_field.verbose_name},
                )
        return username
