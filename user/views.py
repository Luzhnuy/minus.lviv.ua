from django.shortcuts import render
from user.models import Userprofile,UsersUserrating
from minus.models import DjangoComments,DjangobbForumPost
from minusstore.models import MinusstoreMinusauthor,MinusstoreMinusrecord
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm,EmailAuthenticationForm
import datetime


def user_page(request,pk):
    user = Userprofile.objects.get(user_id = pk)
    user.comments = DjangoComments.objects.filter(user_id = user.user_id).order_by('-id')[:3]
    user.forum = DjangobbForumPost.objects.filter(user_id = user.user_id).order_by('-id')[:3]
    user.u = User.objects.get(pk = user.user_id)
    user.rating = UsersUserrating.objects.get(user_id = user.u.id)
    return render(request, 'user/index.html', {
        'user':user,
	})



def userlist(request):
    users = User.objects.all()
    paginator = Paginator(users, 25)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
        print('first')
    except PageNotAnInteger:
        users = paginator.page(1)
        print('second')
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
        print('third')

    return render(request,'user/list.html',{'users':users})

class RegisterFormView(FormView):
    form_class = UserCreateForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "http://127.0.0.1:8000"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "user/registration.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        self.last_login = datetime.datetime.now()
        form.save()

        return super(RegisterFormView, self).form_valid(form)





class UserLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'user/false_auth.html'
    redirect_authenticated_user = True

    def post(self, request, *args, **kwargs):

        form = self.get_form()  # type: AuthenticationForm
        if form.is_valid():
            print('kek')
            return self.form_valid(form)
        else:

            if 'username' in form.cleaned_data:
                username = form.cleaned_data['username']
                print('sobaka')
                try:
                    print('lol')
                    User.objects.get(username=username)
                except User.DoesNotExist:
                    return HttpResponseRedirect('../../')
                    print('sobaka2')

            return self.form_invalid(form)


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('../../')


def userminuses(request,user_id):
    minuses = MinusstoreMinusrecord.objects.filter(user_id=user_id).order_by('-id')
    paginator = Paginator(minuses, 10)
    page = request.GET.get('page')
    try:
        minuses = paginator.page(page)
        print('first')
    except PageNotAnInteger:
        minuses = paginator.page(1)
        print('second')
    except EmptyPage:
        minuses = paginator.page(paginator.num_pages)
        print('third')

    return render(request,'user/user_minuses.html', {'minus':minuses})
