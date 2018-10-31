from django.shortcuts import render
from minus.models import MinusstoreMinusplusrecord,MinusstoreMinusrecord

def plusstore_main(request):
	plus = MinusstoreMinusrecord.objects.all()[:20]
	
	
	return render(request,'plusstore/plusstore.html',{
		'plus':plus,
	})	