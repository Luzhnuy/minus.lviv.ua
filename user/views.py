from django.shortcuts import render
from user.models import AuthUser,Userprofile,UsersUserrating
from minus.models import DjangoComments
from minusstore.models import MinusstoreMinusauthor
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
from .forms import UserCreateForm
import datetime


def user_page(request,pk):
    user = Userprofile.objects.get(user_id = pk)
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
    form_class = AuthenticationForm
    template_name = 'mytags/login.html'
    redirect_authenticated_user = True

    def post(self, request, *args, **kwargs):

        form = self.get_form()  # type: AuthenticationForm
        if form.is_valid():
            return self.form_valid(form)
        else:
            # выведем ошибку если пользователь не существует
            if 'username' in form.cleaned_data:
                username = form.cleaned_data['username']
                try:
                    User.objects.get(username=username)
                except User.DoesNotExist:
                    return HttpResponseRedirect('../../')
                      # не знаю как ещё оставить только одну ошибку

            return self.form_invalid(form)


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('../../')
