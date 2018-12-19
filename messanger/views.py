from django.shortcuts import render
from minus.models import MessagesMessage
from django.contrib.auth.models import User

# Create your views here.

def messanger(request):
    if request.user.is_authenticated:
        all_messages = MessagesMessage.objects.filter(recipient_id = request.user.id)
        sender = []
        for a_m in all_messages:
            sender.append(a_m.sender_id)
        sender = User.objects.filter(id__in = sender)
        return render(request, 'messanger/messanger.html' , {'sender':sender,})



def messages(request,pk):
    if request.user.is_authenticated:
        all_messages = MessagesMessage.objects.filter(recipient_id = request.user.id)
        sender = []
        for a_m in all_messages:
            sender.append(a_m.sender_id)
        sender = User.objects.filter(id__in = sender)
        messages = MessagesMessage.objects.filter(recipient_id=request.user.id,sender_id=pk)
        return render(request, 'messanger/messanger.html' , {'messages':messages,'sender':sender,})
