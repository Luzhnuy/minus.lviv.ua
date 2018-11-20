from django.shortcuts import render,get_object_or_404
from minus.models import DjangoComments,Likedislike
from user.models import AuthUser
from minusstore.models import MinusstoreMinusauthor,MinusstoreMinusrecord,MinusstoreMinusrecordCategories,MinusstoreMinuscategory
from django.http import HttpResponse
from django.core import serializers
from main.forms import AuthForm
from minusstore.forms import AddMinusForm
<<<<<<< HEAD
# from minus.autentification import *

=======
import pdfkit
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
>>>>>>> messanger

# @cache_page(60 * 15)
def minusstore_main(request):
<<<<<<< HEAD
	form = AuthForm(request.POST)
	# signin(request,form)
	author = MinusstoreMinusauthor.objects.all().order_by('name')[:20]
=======
>>>>>>> messanger

	# signin(request,form)
    author = MinusstoreMinusauthor.objects.all().order_by('name')
    paginator = Paginator(author, 40)
    page = request.GET.get('page')
    try:
        author = paginator.page(page)
        print('first')
    except PageNotAnInteger:
        author = paginator.page(1)
        print('second')
    except EmptyPage:
        author = paginator.page(paginator.num_pages)
        print('third')

    return render(request, 'minusstore/index.html' , {

		'author' : author,


		})


<<<<<<< HEAD
def minusstore_minus(request):
		form = AuthForm(request.POST)

		# signin(request,form)
		minus = get_object_or_404(MinusstoreMinusrecord,pk=pk)
		author = get_object_or_404(MinusstoreMinusauthor,pk=minus.author_id)
		comments = DjangoComments.objects.filter(object_pk=minus.pk,content_type_id=17)
		minus_user = get_object_or_404(AuthUser,pk=minus.user_id)
		upload_minuses_from_user = MinusstoreMinusrecord.objects.filter(user_id=minus_user.id).count()
		return render(request, 'minusstore/minus.html' , {
		'minus' : minus,
		'author' : author,
		'comments' : comments,
		'minus_user':minus_user,
		'upload_minuses' : upload_minuses_from_user,

		})
=======
def minusstore_minus(request,pk):

		# signin(request,form)
    minus = get_object_or_404(MinusstoreMinusrecord,pk=pk)
    author = get_object_or_404(MinusstoreMinusauthor,pk=minus.author_id)
    comments = DjangoComments.objects.filter(object_pk=minus.pk,content_type_id=17)
    try:
        likedislike = Likedislike.objects.get(content_type_id= 17,object_id = minus.pk)
    except:
        likedislike = 0
    minus_user = get_object_or_404(AuthUser,pk=minus.user_id)
    upload_minuses_from_user = MinusstoreMinusrecord.objects.filter(user_id=minus_user.id).count()
    minus.filesize = int(minus.filesize/1000000)
    return render(request, 'minusstore/minus.html' , {
        'likedislike' : likedislike,
        'minus' : minus,
        'author' : author,
        'comments' : comments,
        'minus_user':minus_user,
        'upload_minuses' : upload_minuses_from_user,
    })

>>>>>>> messanger

def add_minus(request):
		form = AuthForm(request.POST)
		# signin(request,form)
		form_add_minus = AddMinusForm(request.POST)

		return render(request, 'minusstore/add_minus.html' , {
<<<<<<< HEAD
		"form":form,
=======

>>>>>>> messanger
		"form_add_minus" : form_add_minus,
		})

def if_minus_correct(request,pk):
		form = AuthForm(request.POST)
		minus = MinusstoreMinusrecord.objects.get(pk=pk)
		category_id = MinusstoreMinusrecordCategories.objects.get(minusrecord_id=minus.pk)
		сategory_id = category_id.minuscategory_id
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
    print(text)
    pdf = pdfkit.from_string(text, 'micro.pdf', options=options)
    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="micro.pdf"'
    return response

# @cache_page(60 * 15)
def letters_filter(request,letter):
    author = MinusstoreMinusauthor.objects.filter(name__startswith=letter)
    paginator = Paginator(author, 40)
    page = request.GET.get('page')
    try:
        author = paginator.page(page)
        print('first')
    except PageNotAnInteger:
        author = paginator.page(1)
        print('second')
    except EmptyPage:
        author = paginator.page(paginator.num_pages)
        print('third')


    # for i in author:
    #     i.minus = MinusstoreMinusrecord.objects.filter(author_id=i.pk)
    # for m in minus:
    # 	print(m.author.name)

	# for a in author:
    #     a.minus = []
    #     for m in minus:
    #         if m.author_id == a.id:
    #             a.minus.append(m)

    return render(request, 'minusstore/index.html' , {'author' : author,'letter':letter})

def gave(request,author_id):
    minuss = MinusstoreMinusrecord.objects.filter(author_id=int(author_id))
    minuss = serializers.serialize("json",minuss)
    return HttpResponse(minuss)
