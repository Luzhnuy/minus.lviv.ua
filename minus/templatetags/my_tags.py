from django import template
from minus.new_minuses import *
from minus.tops_functions import *
from minus.new_minuses import *

register = template.Library()


@register.inclusion_tag('mytags/minus_per_all_time.html')
def minus_per_all_time():
	return {'minus_top_all_time' : top_minus_per_all_time() }

@register.inclusion_tag('mytags/minus_per_week.html')
def minus_per_week():
	return {'minus_top_week' : top_minus_per_week()}	

@register.inclusion_tag('mytags/top_user.html')
def top_u():
	return {'top_users' : top_users()}

@register.inclusion_tag('mytags/new_m.html')
def new_m():
	return {'new_m':new_minuses()}	

@register.inclusion_tag('mytags/last_forum.html')
def last_f():
	return {'forum' : last_forum()}