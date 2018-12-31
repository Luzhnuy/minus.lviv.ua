from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from shop.models import BlurbsBlurb,BlurbsGeoregion
from user.models import Userprofile
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView
from shop.forms import BlurbForm



def main_shop(request):
	good = BlurbsBlurb.objects.all().order_by('-id')
	georegion = BlurbsGeoregion.objects.all()
	paginator = Paginator(good, 40)
	page = request.GET.get('page')
	try:
	    good = paginator.page(page)

	except PageNotAnInteger:
	    good = paginator.page(1)
	       # print('second')
	except EmptyPage:
	    good = paginator.page(paginator.num_pages)
	        #print('third')


	return render(request, 'shop/index.html' , {
		'goods':good,
		'georegion':georegion,

	})
def goods(request,pk):
	good = BlurbsBlurb.objects.get(pk=pk)

	return render(request, 'shop/goods.html' , {'good':good,})



def gave_business_or_private(request,bool):
	#goods = []
	good = None
	if bool == '1':
		good = BlurbsBlurb.objects.filter(is_user_business=1)
		paginator = Paginator(good, 40)
		page = request.GET.get('page')
		try:
		    good = paginator.page(page)
		except PageNotAnInteger:
			good = paginator.page(1)

		except EmptyPage:
		    good = paginator.page(paginator.num_pages)

		return render(request, 'shop/index.html',{'goods':good,'z':True,})

	else:
		good = BlurbsBlurb.objects.filter(is_user_business=0)
		paginator = Paginator(good, 40)
		page = request.GET.get('page')
		try:
		    good = paginator.page(page)
		except PageNotAnInteger:
			good = paginator.page(1)
		except EmptyPage:
		    good = paginator.page(paginator.num_pages)
		return render(request, 'shop/index.html',{'goods':good,'f':True,})



def add_blurb(request):
	if request.user.is_authenticated:
		blurb_form = BlurbForm(request.POST or None,request.FILES or None)
		if request.method == 'POST':
			print('method POST')
			# blurb_form.is_valid = True

			# blurb_form.errors= False
			if blurb_form.is_valid():
				blurb_form_s = blurb_form.save(commit=False)
				print('form valid kostul zbc')
				blurb_form_s.user = request.user
				blurb_form_s.is_user_business = Userprofile.objects.get(user_id = request.user.id).is_business
				blurb_form_s.category_id = request.POST.get('category')
				blurb_form_s.title = request.POST.get('title')
				blurb_form_s.buysell = request.POST.get('buysell')
				blurb_form_s.description = request.POST.get('description')
				blurb_form_s.georegion_id = request.POST.get('georegion')
				blurb_form_s.cost = request.POST.get('cost')
				try:
					blurb_form_s.first_photo = request.FILES.get('first_photo')
					blurb_form_s.second_photo = request.FILES.get('second_photo')
					blurb_form_s.third_photo = request.FILES.get('third_photo')
				except:
					print('error with files')

				blurb_form_s.save()
				#
				# print('form valid')
				# # blurb_form_s = blurb_form.save(commit=False)
				# # blurb_form_s.user = request.user
				# print('user')
				# # blurb_form_s.category_id = request.POST['category']
				# print('category')
				#
				# print('business')

			# else:
				# print('form invalid')
		return render(request, 'shop/add_blurb.html', {
			'form':blurb_form,
		})
	else:
		return HttpResponseRedirect('../')
