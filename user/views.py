from django.shortcuts import render
from user.models import Userprofile, UsersUserrating, FriendsFriendshipFriends, UserActivitys
from minus.models import DjangoComments, ForumPost
from minusstore.models import MinusstoreMinusauthor, MinusstoreMinusrecord
from main.models import ModeratorMessages
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm, EmailAuthenticationForm
from user.tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from user.filter import UserFilter
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import lxml.html
import datetime
import json


def user_page(request, pk):
    user = Userprofile.objects.get(user_id=pk)
    user.comments = DjangoComments.objects.filter(user_id=user.user_id).order_by('-id')[:3]
    user.forum = ForumPost.objects.filter(author_id=user.user_id).order_by('-id')[:3]
    for u_f in user.forum:
        u_f.body = lxml.html.fromstring(u_f.body).text_content()
    user.u = User.objects.get(pk=user.user_id)
    try:
        user.rating = UsersUserrating.objects.get(user_id=user.u.id)
    except UsersUserrating:
        user.rating = 0
    return render(request, 'user/index.html', {
        'user': user,
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

    return render(request, 'user/list.html', {'users': users})


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
        # self.is_active = False
        print('hello every_body1')
        form_data = form.save()
        print('hello every_body2')
        print(form_data)
        # form_data.is_active = 0
        current_site = get_current_site(self.request)
        print('hello every_body3')
        print(current_site.domain)
        mail_subject = 'Активація акаунту minus.lviv.ua'
        message = render_to_string('user/sucees_registration.html', {
            'user': form_data,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(form_data.id)),
            'token': account_activation_token.make_token(form_data),
        })
        print('hello every_body4')

        to_email = form_data.email
        print('hello5')
        print(to_email)
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        print(email)
        print('hello6')
        print(form_data.id)
        email.send()

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
                    print('sobaka2')
                    return HttpResponseRedirect('../../')


            return self.form_invalid(form)


def false_auth(request):
    return render(request, 'user/false_auth.html', {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('../../')


def userminuses(request, user_id):
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

    return render(request, 'user/user_minuses.html', {'minus': minuses})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request, 'user/succes_reg_true.html', {})
    else:
        return HttpResponse('Вибачте але лінк активації якийсь поганий(')


def user_search(request):
    # users_all = User.objects.all(
    # users = UserFilter(request.GET, queryset=users_all)
    users = User.objects.filter(Q(first_name__startswith=request.GET['search']) | Q(last_name__startswith=request.GET['search'])| Q(username__startswith=request.GET['search'])| Q(email__startswith=request.GET['search']))
    print('---------------------------------------------')
    print(users)
    print('-----------------------------------------')
    # users = users.qs
    print('gello')
    print(users)
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

    return render(request, 'user/list.html', {'users': users})


def activities(request):
    last_forum = ForumPost.objects.order_by('-id')[:10]
    last_comments = DjangoComments.objects.order_by('-id')[:30]
    if request.user.is_authenticated:
        activities = UserActivitys.objects.filter(to_user_id=request.user.id)
        z = True
    else:
        activities = UserActivitys.objects.all()
        z = False
    return render(request, 'user/activities.html', {
        'activities': activities,
        'z': z,
        'last_forum': last_forum,
        'last_comments': last_comments,
    })

def moderator_messages(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            moderator_messages = ModeratorMessages.objects.all().order_by('-id')
            return render(request,'user/moderator_messages.html',{'moderator_messages':moderator_messages,})



def add_moderator_message(request,object_pk,content_id):
    if request.user.is_authenticated:
        if content_id == '17':
            minus = MinusstoreMinusrecord.objects.get(id = object_pk)
            print(minus.author)
            print(minus.title)
            ModeratorMessages.objects.create(object_pk=object_pk,content_id=content_id,user=request.user,attention_message="Повідомлення про мінусовку"+minus.title)
            return HttpResponseRedirect('/minusstore/minus/'+object_pk+'/')




# API

class GetUser(APIView):
    
    # permission_classes = (IsAuthenticated,) 


    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404


    def get(self, request,pk ,format=None):
        
        
        user = self.get_object(pk = pk)
        user = UserSerializer(user,many=False)


        return Response(user.data)