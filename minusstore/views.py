from django.shortcuts import render,get_object_or_404, redirect
from minus.models import DjangoComments, Likedislike, DeliverySubscriber
from minusstore.models import Minusgenre, Minusappointment, MinusstoreMinusauthor, MinusstoreMinusrecord, \
    MinusstoreMinusrecordCategories, MinusstoreMinuscategory, \
    MinusstoreMinusplusrecord, MinusstoreMinusrecordCategories, MinusstoreFiletype, MinusstoreMinusquality, \
    MinusstoreMinusarrangement
from past.builtins import reduce
from user.models import UserActivitys, SubscribeOnComments
import os
import pdfkit
import datetime
import operator
from mutagen.mp3 import MP3
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from main.forms import AuthForm,AddComments
from minusstore.forms import AddMinusForm
from django.contrib.auth.models import User
from django.views.generic.edit import FormView,UpdateView
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.core.files.storage import default_storage
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from minusstore.serializers import MinusAuthorSerializer
from haystack.query import SearchQuerySet


# @cache_page(60 * 15)
def minusstore_main(request):
    if request.GET:
        if request.GET['category']:
            print(request.GET.getlist('category'))
            for search_item in request.GET.getlist('category'):
                filtred_categories = SearchQuerySet().models(MinusstoreMinuscategory).filter(
                    Q(display_name__fuzzy = search_item) |
                    Q(name__fuzzy = search_item)
                )
                print(len(filtred_categories.all()))

    author = MinusstoreMinusauthor.objects.order_by('name').filter(Q(name__startswith = 'А') | Q(name__startswith = "a"))
    folk_minus = MinusstoreMinusrecord.objects.order_by('title').filter(Q(title__startswith = 'А') | Q(title__startswith = "a"),is_folk=1)

    return render(request, 'minusstore/index.html' , {
        'folk_minus' : folk_minus,
		'author' : author,
    })

def minusstore_minus(request,pk):
    minus = get_object_or_404(MinusstoreMinusrecord,pk=pk)
    author = get_object_or_404(MinusstoreMinusauthor,pk=minus.author_id)
    quality_rate = MinusstoreMinusquality.objects.filter(minus_id = minus.id)
    count_quality_rate = quality_rate.count()
    arrangement_rate = MinusstoreMinusarrangement.objects.filter(minus_id = minus.id)
    count_arrangement_rate = arrangement_rate.count()
    sum_q_rate = 0
    for q_rate in quality_rate:
        sum_q_rate = sum_q_rate + q_rate.rate

    try:
        quality_rate = sum_q_rate/count_quality_rate
    except ZeroDivisionError:
        quality_rate = 0
    sum_a_rate = 0

    for a_rate in arrangement_rate:
        sum_a_rate = sum_a_rate + a_rate.rate

    try:
        arrangement_rate = sum_a_rate/count_arrangement_rate
    except ZeroDivisionError:
        arrangement_rate = 0

    minus.all_rate = (quality_rate+arrangement_rate) / 2
    minus.comments = DjangoComments.objects.filter(object_pk=minus.pk, content_type_id=17)

    for c in minus.comments:
        c.answer = DjangoComments.objects.filter(object_pk = c.id, content_type_id = 45)
        c.likes = Likedislike.objects.filter(type_id= 45,object_id = c.pk,likes=1).count()
        c.dislikes = Likedislike.objects.filter(type_id= 45,object_id = c.pk,likes=0).count()
    try:
        minus.plusrecord = MinusstoreMinusplusrecord.objects.get(minus_id=minus.id)
    except MinusstoreMinusplusrecord.DoesNotExist:
        minus.plusrecord=None

    likes = Likedislike.objects.filter(type_id= 17,object_id = minus.pk,likes=1).count()

    dislikes = Likedislike.objects.filter(type_id= 17,object_id = minus.pk,likes=0).count()

    minus_user = get_object_or_404(User,pk=minus.user_id)
    upload_minuses_from_user = MinusstoreMinusrecord.objects.filter(user_id=minus_user.id).count()
    minus.filesize = int(minus.filesize/1000000)
    add_comment_form = AddComments(request.POST)

    if request.user.is_authenticated:
        try:
            arrangement_assessment = MinusstoreMinusarrangement.objects.get(user_id = request.user.id,minus_id = minus.id)
            minus.arrangement_assessment = arrangement_assessment.rate
        except MinusstoreMinusarrangement.DoesNotExist:
            minus.arrangement_assessment = ''
        try:
            quality_assessment = MinusstoreMinusquality.objects.get(user_id = request.user.id, minus_id = minus.id)
            print('quality assessment >')
            print(quality_assessment.rate)
            minus.quality_assessment = quality_assessment.rate
        except MinusstoreMinusquality.DoesNotExist:
            minus.quality_assessment = ''
        if request.method == "POST":
            if add_comment_form.is_valid():
                comment = add_comment_form.cleaned_data['comment']
                if comment[0] == "@":
                    comment = comment.split(" ")
                    user = comment[0]
                    comment_id = user.split('#')
                    comment_id = comment_id[1]

                    comment = user[0]
                    add_comment = add_comment_form.save(commit=True,pk=comment_id,request=request,content_type_id=45)
                else:
                    add_comment = add_comment_form.save(commit=True,pk=pk,request=request,content_type_id=17)
                if request.POST.get('subscribe'):
                    for subscriber in SubscribeOnComments.objects.filter(content_type_id = 51, object_pk = pk):
                        UserActivitys.objects.create(from_user = request.user,type='s',to_user_id = subscriber.user.id,activity_to=pk)
                    try:
                        SubscribeOnComments.objects.get(content_type_id = 51,object_pk = pk, user = request.user)
                    except SubscribeOnComments.DoesNotExist:
                        SubscribeOnComments.objects.create(
							content_type_id=51,
							object_pk = pk,
							user = request.user
						)
                return render(request, 'minusstore/minus.html' , {
                    'likes' : likes,
                    'dislikes' : dislikes,
                    'minus' : minus,
                    'author' : author,
                    'minus_user':minus_user,
                    'upload_minuses' : upload_minuses_from_user,
                    'add_comment_form':add_comment_form,
                })
    return render(request, 'minusstore/minus.html' , {
        'likes' : likes,
        'dislikes' : dislikes,
        'minus' : minus,
        'author' : author,
        'minus_user':minus_user,
        'upload_minuses' : upload_minuses_from_user,
        'add_comment_form':add_comment_form,
    })


def if_minus_correct(request,pk):
    form = AuthForm(request.POST)
    minus = MinusstoreMinusrecord.objects.get(pk=pk)
    try:
        category_id = MinusstoreMinusrecordCategories.objects.get(minusrecord_id=minus.pk)
        сategory_id = category_id.minuscategory_id
    except MinusstoreMinusrecordCategories.DoesNotExist:
        category_id = None

    minus.author = MinusstoreMinusauthor.objects.get(pk = minus.author_id)
		# category = MinusstoreMinuscategory.objects.get(pk=category_id)

    return render(request, 'minusstore/look_on_minus_correct.html' , {

		'minus':minus,
		# 'category':category,

	})


def pdf_generete(request,pk):
    options = {

    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    }
    minus = get_object_or_404(MinusstoreMinusrecord,pk=pk)
    text= "<h1>"+minus.lyrics+"</h1>"

    pdf = pdfkit.from_string(text, 'micro.pdf', options=options)
    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="micro.pdf"'
    return response

# @cache_page(60 * 15)
def letters_filter(request,letter):
    author = MinusstoreMinusauthor.objects.filter(name__startswith=letter)

    minus_folk = MinusstoreMinusrecord.objects.filter(title__startswith=letter,is_folk=1)


    return render(request, 'minusstore/index.html' , {'author' : author,'letter':letter,'minus_folk':minus_folk})

def gave(request,author_id):
    minuss = MinusstoreMinusrecord.objects.filter(author_id=int(author_id))
    minuss = serializers.serialize("json",minuss)
    return HttpResponse(minuss)


def archiv_of_minuses(request,day):
    date = datetime.date.today()
    minuses = MinusstoreMinusrecord.objects.filter(pub_date__year=date.year,pub_date__month=date.month,pub_date__day=day)
    paginator = Paginator(minuses, 10)
    page = request.GET.get('page')
    try:
        minuses = paginator.page(page)
    except PageNotAnInteger:
        minuses = paginator.page(1)

    except EmptyPage:
        minuses = paginator.page(paginator.num_pages)

    # minus = MinusstoreMinusrecord.objects.filter(pub_date__year='2015',pub_date__month='6'.month,pub_date__day=day)
    return render(request,'user/user_minuses.html',{'minus':minuses,'z':day,})

def subscribe(request):
    if request.user.is_authenticated:
        subscriber = DeliverySubscriber.objects.create(email = request.user.email,is_subscribed=1,frequency='weekly',hash="214213a",date=datetime.datetime.now())
        subscriber.save()
        z = "Вітаємо ви підписались на оновлення мінусовок!!"
        k = "Тепер кожного тижня вам на пошту будуть приходити списки нових мінусовок"
        return render(request,'minusstore/subscribed.html',{'z':z,'k':k})
    else:
        z = "Вибачте шоб підписати на оновлення вам потрібно увійти"
        k = "Щоб увійти перейдіть у 'Закуліси'"

        return render(request,'minusstore/subscribed.html',{
            'z':z,
            'k':k
        })

def all_minuses_by_date(request):
    minuses = MinusstoreMinusrecord.objects.order_by('-pub_date')
    paginator = Paginator(minuses, 40)
    page = request.GET.get('page')
    try:
        minuses = paginator.page(page)
    except PageNotAnInteger:
        minuses = paginator.page(1)
    except EmptyPage:
        minuses = paginator.page(paginator.num_pages)

    return render(request, 'user/user_minuses.html', {'minus': minuses,'all_minuses':True})

def add_minus(request):
    if request.user.is_authenticated:

        form_add_minus = AddMinusForm(request.POST)
        minuscategory = MinusstoreMinuscategory.objects.all()[::20]
        minustype = MinusstoreFiletype.objects.all()
        if request.method == "POST" and request.FILES:
            form_add_minus = AddMinusForm(request.FILES, request.POST)
            if form_add_minus.is_valid():
                minusrecord = form_add_minus.save(commit=False)
                z = False
                for i in MinusstoreMinusauthor.objects.all():
                    if minusrecord.author.lower() == i.name.lower():
                        minusrecord.author = i
                            # Якщо воно стане тру то воно найшло такого автора і записало
                        z = True
                    else:
                        continue
                    # Якщо фолс то воно не знайшло такого автора і створить нового
                if z == False:
                     MinusstoreMinusauthor.objects.create(name=minusrecord.author)
                     minusrecord.author = MinusstoreMinusauthor.objects.latest('id')





                # minusrcord.bitrate = f.info.bitrate/1000
                # minusrecord.length = f.info.length
                minusrecord.user=request.user

                minusrecord.save()




                if request.FILES['plus']:
                    MinusstoreMinusplusrecord.objects.create(minus_id = MinusstoreMinusrecord.objects.latest('id'),user_id = request.user.id,file=request.FILES['plusrecord'])

                minusrecord.save()
                return HttpResponseRedirect('add_minus')
            else:
                print("NOT VALID !!! NOT VALID !!!")
                return render(request, 'minusstore/add_minus.html' , {
                    'minuscategory':minuscategory,
            	    "form_add_minus" : form_add_minus,
                    'minustype' : minustype,
            	})
        else:
            form_add_minus = AddMinusForm()
            return render(request, 'minusstore/add_minus.html' , {
                'minuscategory':minuscategory,
        	    "form_add_minus" : form_add_minus,
                'minustype' : minustype,
        	})



    else:

        return HttpResponseRedirect('../../')




class MinusRecordUpdate(UpdateView):
    model = MinusstoreMinusrecord
    fields = ['title','file','annotation','minus_genre','minus_appointment','lyrics','plusrecord']
    template_name_suffix = '_update_form'

def minus_search(request):
    minuses = MinusstoreMinusrecord.objects.filter(title__startswith = request.GET['search'])
    paginator = Paginator(minuses, 40)
    page = request.GET.get('page')
    try:
        minuses = paginator.page(page)

    except PageNotAnInteger:
        minuses = paginator.page(1)

    except EmptyPage:
        minuses = paginator.page(paginator.num_pages)


    return render(request,'user/user_minuses.html',{'minus':minuses,'k':True})




# API
def minusarrangement(request,user_id,minus_id,assessment):
    try:
        minus_arrangement = MinusstoreMinusarrangement.objects.get(minus_id = minus_id, user_id = user_id)
        minus_arrangement.rate = assessment
        minus_arrangement.save()
        return HttpResponse(assessment)

    except MinusstoreMinusarrangement.DoesNotExist:
        minus_arrangement = MinusstoreMinusarrangement.objects.create(minus_id = minus_id, user_id = user_id , rate = assessment)
        minus_arrangement.save()
        return HttpResponse(assessment)


def minusquality(request,user_id,minus_id,assessment):
    try:
        minus_quality = MinusstoreMinusquality.objects.get(minus_id = minus_id, user_id = user_id)
        minus_quality.rate = assessment
        minus_quality.save()
        return HttpResponse(assessment)

    except MinusstoreMinusquality.DoesNotExist:
        minus_quality = MinusstoreMinusquality.objects.create(minus_id = minus_id, user_id = user_id , rate = assessment)
        minus_quality.save()
        return HttpResponse(assessment)


class MinusAuthor(APIView):
    def get_objects(self, letter):

        return MinusstoreMinusauthor.objects.filter(name__startswith=letter)

    def get(self, request, letter='А', format=None):
        authors=self.get_objects(letter)
        paginator = Paginator(authors, 40)
        page = self.request.GET.get('page')
        try:
            authors = paginator.page(page)

        except PageNotAnInteger:
            authors = paginator.page(1)

        except EmptyPage:
            authors = paginator.page(paginator.num_pages)


        serializer_context = {
                'request': request,
            }
        authors = MinusAuthorSerializer(authors,many=True, context = serializer_context)
        return Response(authors.data)
