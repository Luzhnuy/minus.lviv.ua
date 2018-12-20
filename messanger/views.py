from django.shortcuts import render
from minus.models import MessagesMessage
from django.contrib.auth.models import User
# from messanger.filters import MessageFilter

# Create your views here.

def messanger(request):
    if request.user.is_authenticated:
        all_messages = MessagesMessage.objects.all()
        # all_messages=MessageFilter(request.user.id,queryset=all_messages)
        sender = []
        recipient = []
        for a_m in all_messages:
            if a_m.recipient_id == request.user.id or a_m.sender_id == request.user.id:
                sender.append(a_m.sender_id)
            # recipient.append(a_m)
            # sender = sender+recipient
        sender = User.objects.filter(id__in = sender).order_by('-id')
        return render(request, 'messanger/messanger.html' , {'sender':sender,})



def messages(request,pk):
    if request.user.is_authenticated:
        all_messages = MessagesMessage.objects.all()
        # all_messages=MessageFilter(request.user.id,queryset=all_messages)
        sender = []
        messages = []
        for a_m in all_messages:
            if a_m.recipient_id == request.user.id or a_m.sender_id == request.user.id:
                sender.append(a_m.sender_id)
                messages.append(a_m)
        sender = User.objects.filter(id__in = sender)
        # messages = MessagesMessage.objects.filter(recipient_id=request.user.id,sender_id=pk)

        return render(request, 'messanger/messanger.html' , {'messages':messages,'sender':sender,'pk':pk,})
