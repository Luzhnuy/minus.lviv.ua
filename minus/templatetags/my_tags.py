from django import template
from minus.new_minuses import *
from minus.tops_functions import *
import datetime
from user.models import UsersUserrating,Userprofile
from main.forms import AuthForm
from django.views.decorators.cache import cache_page
from messanger.models import Channels

register = template.Library()


@register.inclusion_tag('mytags/minus_per_all_time.html')
def minus_per_all_time():
	return {'minus_top_all_time' : top_minus_per_all_time() }

@register.inclusion_tag('mytags/minus_per_week.html')
def minus_per_week():
	return {'minus_top_week' : top_minus_per_week()}

@register.inclusion_tag('mytags/top_user.html')
def top_u():
	users = top_users()

	return {
		'top_users' : users,
		# 'rating' : rate,
	}

@register.inclusion_tag('mytags/new_m.html')
def new_m():
	return {'new_m':new_minuses()}

@register.inclusion_tag('mytags/last_minuses.html')
def last_minuses():
	return {'new_m':new_minuses()}

@register.inclusion_tag('mytags/last_forum.html')
def last_f():
	return {'forum' : last_forum()}


@register.inclusion_tag('mytags/login.html')
def login():
	form = AuthForm()
	return 	{'form':form }

@register.inclusion_tag('mytags/letters.html')
def letters():
	pass

@register.inclusion_tag('mytags/len_shame.html')
def count_shame():
	banned_users = []
	users = Userprofile.objects.filter(banned=1)
	for u in users:
		if u.banned_until>datetime.date.today():
			banned_users.append(u)
	return {'len':len(banned_users)}



@register.inclusion_tag('mytags/user_online.html')
def user_online():
	users = Channels.objects.filter(is_active=1)
	users = Userprofile.objects.filter(user_id__in=users.values_list('user_id'))
	return {'users_online':users,'len':0,}
