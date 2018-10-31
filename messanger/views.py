from django.shortcuts import render

# Create your views here.
 
def messanger(request):
	return render(request, 'messanger/messanger.html' , {})
