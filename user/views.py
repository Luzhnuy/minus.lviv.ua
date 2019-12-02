from django.shortcuts import render
from user.models import Userprofile, UsersUserrating, FriendsFriendshipFriends,FriendsFriendship, FriendsFriendshiprequest,UserActivitys,UserPost
from minus.models import DjangoComments, ForumPost
from messanger.models import Channels
from album.models import PhotosPhotoalbum,PhotosPhoto
from minusstore.models import MinusstoreMinusauthor, MinusstoreMinusrecord
from main.models import ModeratorMessages
from shop.models import BlurbsBlurb,SelectedBlurb
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView,UpdateView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm, EmailAuthenticationForm,AddUserPost,AddModeratorMessagesForm,AddPhotoForm
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
    user=Userprofile.objects.get(user_id=pk)
    try:
        friendship=FriendsFriendship.objects.get(user_id = user.user.id)
    except FriendsFriendship.DoesNotExist:
        friendship = 0

    friendshipfriends=FriendsFriendshipFriends.objects.filter(from_friendship_id=friendship.id).order_by('-id')
    friendship_id = friendshipfriends.values_list('to_friendship_id')
    friends=FriendsFriendship.objects.filter(id__in=friendship_id).order_by('-id')[:10]
    user.comments = DjangoComments.objects.filter(user_id=user.user_id).order_by('-id')[:10]
    user.forum = ForumPost.objects.filter(author_id=user.user_id).order_by('-id')[:10]
    for u_f in user.forum:
        u_f.body = lxml.html.fromstring(u_f.body).text_content()

    # user.u = User.objects.get(pk=user.user_id)
    is_friend=0
    add_post_form = AddUserPost(request.POST,request.FILES)
    if request.user.is_authenticated:
        for f in friends:
            if f.user_id==request.user.id:
                is_friend=1
        if request.method == "POST":
            if add_post_form.is_valid():
                print("addING POST")
                add_post = add_post_form.save(request,commit=True)



    try:
        user.rating = UsersUserrating.objects.get(user_id=user.user.id)
    except UsersUserrating:
        user.rating = 0
    user_post = UserPost.objects.filter(userprofile_id = user.id).order_by('-pub_date')
    return render(request, 'user/index.html', {
        'user': user,
        'friends':friends,
        'is_friend':is_friend,
        'posts':user_post,
        'add_post_form':add_post_form,
    })



class ProfileUpdate(UpdateView):
    model = Userprofile
    fields = ['gender','city','country','avatar','birthdate','icq','skype','website','about',]
    template_name_suffix = '_update_form'

def all_friends(request,pk):
    try:
        friendship=FriendsFriendship.objects.get(user_id = pk)
    except FriendsFriendship.DoesNotExist:
        friendship = 0

    friendshipfriends=FriendsFriendshipFriends.objects.filter(from_friendship_id=friendship.id).order_by('-id')
    friendship_id = friendshipfriends.values_list('to_friendship_id')
    friends=FriendsFriendship.objects.filter(id__in=friendship_id).order_by('-id')
    friends_request = FriendsFriendshiprequest.objects.filter(to_user_id=request.user.id)

    return render(request, 'user/all_friends.html', {
        'friends_request':friends_requests,
        'users':friends,
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
        form_data = form.save()
        # form_data.is_active = 0
        current_site = get_current_site(self.request)
        mail_subject = 'Активація акаунту minus.lviv.ua'
        message = render_to_string('user/sucees_registration.html', {
            'user': form_data,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(form_data.id)),
            'token': account_activation_token.make_token(form_data),
        })

        to_email = form_data.email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()

        return super(RegisterFormView, self).form_valid(form)

def advertisement(request):
    if request.user.is_authenticated:
        z = True
        selected_blurbs = SelectedBlurb.objects.filter(user_id = request.user.id)
        blurbs = BlurbsBlurb.objects.filter(user_id = request.user.id)
        try:
            blurbs = paginator.page(page)
            print('first')
        except PageNotAnInteger:
            blurbs = paginator.page(1)
            print('second')
        except EmptyPage:
            blurbs = paginator.page(paginator.num_pages)
            print('third')
        for g in blurbs:
            try:
                ph_a = PhotosPhotoalbum.objects.get(content_type_id=52,object_pk = g.id)
                g.photo = PhotosPhoto.objects.filter(album_id = ph_a.id)
                try:
                    g.photo = g.photo[0].image
                except:
                    g.photo='pass'
            except PhotosPhotoalbum.DoesNotExist:
			# print("except")
                g.photo = "http://praktikaprava.ru/wp-content/uploads/2017/11/obmen-tovara-v-techenii-14-dnej.jpg"
            # print("end--------------------")
        for g in selected_blurbs:
            try:
                ph_a = PhotosPhotoalbum.objects.get(content_type_id=52,object_pk = g.blurb.id)
                g.photo = PhotosPhoto.objects.filter(album_id = ph_a.id)
                try:
                    g.photo = g.photo[0].image
                except:
                    g.photo='pass'
            except PhotosPhotoalbum.DoesNotExist:
                g.photo = "http://praktikaprava.ru/wp-content/uploads/2017/11/obmen-tovara-v-techenii-14-dnej.jpg"
        return render(request, 'user/user_goods.html',{'blurbs':blurbs,'selected_blurbs':selected_blurbs,'z':z,})

class AddPhoto(FormView):
    form_class = AddPhotoForm
    template_name = "user/add_photo.html"
    success_url = '/'

    def form_valid(self, form):
        print(self.request.user.id)
        photo_album = PhotosPhotoalbum.objects.get(content_type_id = 20,user_id = self.request.user.id)
        form.instance.album = photo_album
        return super().form_valid(form)


def delete_selected_blurbs(request, pk):
    if request.user.is_authenticated:
        selected_blurb = SelectedBlurb.objects.get(pk=pk).delete()
        return HttpResponseRedirect('/user/user-advertisement/')

class UserLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'user/false_auth.html'
    redirect_authenticated_user = True

    def post(self, request, *args, **kwargs):

        form = self.get_form()  # type: AuthenticationForm
        if form.is_valid():
            return self.form_valid(form)
        else:

            if 'username' in form.cleaned_data:
                username = form.cleaned_data['username']
                try:
                    user = User.objects.get(username=username)
                    userprofile = Userprofile.objects.get(user_id = user.id)
                except User.DoesNotExist:
                    return HttpResponseRedirect('../../')

            return self.form_invalid(form)


def false_auth(request):
    return render(request, 'user/false_auth.html', {})


def logout_view(request):
    Channels.objects.get(user_id=request.user.pk).delete()
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


def user_goods(request,user_id):
    blurbs = BlurbsBlurb.objects.filter(user_id = user_id)
    paginator = Paginator(blurbs, 10)
    page = request.GET.get('page')
    try:
        blurbs = paginator.page(page)
        print('first')
    except PageNotAnInteger:
        blurbs = paginator.page(1)
        print('second')
    except EmptyPage:
        blurbs = paginator.page(paginator.num_pages)
        print('third')
    for g in blurbs:
        print("work hard")
        try:
            print("try")
            ph_a = PhotosPhotoalbum.objects.get(content_type_id=52,object_pk = g.id)
            g.photo = PhotosPhoto.objects.filter(album_id = ph_a.id)
            try:
                g.photo = g.photo[0].image
            except:
                g.photo='pass'
        except PhotosPhotoalbum.DoesNotExist:
            print("except")
            g.photo = "http://praktikaprava.ru/wp-content/uploads/2017/11/obmen-tovara-v-techenii-14-dnej.jpg"
        print("end--------------------")
    return render(request, 'user/user_goods.html',{'blurbs':blurbs,})

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
        return render(request, 'user/succes_reg_true.html', {})
    else:
        return HttpResponse('Вибачте але лінк активації якийсь поганий(')


def user_search(request):
    users = User.objects.filter(
        Q(first_name__startswith=request.GET['search']) | Q(last_name__startswith=request.GET['search'])| Q(username__startswith=request.GET['search'])| Q(email__startswith=request.GET['search'])
    )
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
    form = AddModeratorMessagesForm(request.POST)
    if request.method == "POST":

        if request.user.is_authenticated:

            print("form prevalidation")
            if form.is_valid():
                print("form moderator_messages is valid")
                # if content_id == '17':
                    # minus = MinusstoreMinusrecord.objects.get(id = object_pk)
                    # print(minus.author)
                    # print(minus.title)
                    # ModeratorMessages.objects.create(object_pk=object_pk,content_id=content_id,user=request.user,attention_message="Повідомлення про мінусовку"+minus.title)
                form = form.save(request,content_id,object_pk,commit=True)
    return render(request, 'user/add_moderator_messages.html', {'form':form,})



# def list_friends_request(request):
#     if request.user.is_authenticated:
#         friends_request =  FriendsFriendshiprequest.objects.filter(to_user_id=request.user.id)

def friends_requests(request,pk):
    if request.user.is_authenticated:
        friends_request = FriendsFriendshiprequest.objects.filter(to_user_id=request.user.id)
        return render(request,'user/friends_requests.html',{'friends_request':friends_requests
        })


# API
class FriendsRequest(APIView):
    def get(self,request,to_user_id,format=None):
        print(to_user_id)
        friend_request = FriendsFriendshiprequest.objects.create(from_user_id=request.user.id,to_user_id=to_user_id,accepted=0)
        return Response('{"1":1}')




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
