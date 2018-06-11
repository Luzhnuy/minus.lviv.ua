from django.shortcuts import render
from minus.models import MinusstoreMinusstats, MinusstoreMinusrecord

# Create your views here.

def main(request):
	minus = MinusstoreMinusstats.objects.all()
	minus_id = minus.minus_id
	minus_id = minus_id[:11]
	for i in minus_id:
		 

	return render(request, 'main/index.html')
