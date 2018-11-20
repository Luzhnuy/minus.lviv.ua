from minusstore.models import  MinusstoreMinusrecord

def new_minuses():
	new_m = MinusstoreMinusrecord.objects.filter().order_by("-id")[:10]

	return new_m
