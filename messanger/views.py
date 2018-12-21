from django.shortcuts import render
from minus.models import MessagesMessage
from django.contrib.auth.models import User
from django.db.models import Q
# from messanger.filters import MessageFilter

# Create your views here.

def messanger(request):
    if request.user.is_authenticated:
        sender = MessagesMessage.objects.filter(Q(recipient_id=request.user.id) | Q(sender_id = request.user.id)).values('sender_id','recipient_id')
        # recipient = MessagesMessage.objects.filter(Q(recipient_id=request.user.id) | Q(sender_id = request.user.id)).values(sender_id)
        # all_messages=MessageFilter(request.user.id,queryset=all_messages)
        # sender = []
        # recipient = []
        # for a_m in all_messages:
        #     if a_m.recipient_id == request.user.id or a_m.sender_id == request.user.id:
        #         sender.append(a_m.sender_id)
            # recipient.append(a_m)
            # sender = sender+recipient
        sender = User.objects.filter(Q(id__in = sender.values('sender_id'))|Q(id__in = sender.values('recipient_id'))).order_by('-id')
        return render(request, 'messanger/messanger.html' , {'sender':sender,})



def messages(request,pk):
    if request.user.is_authenticated:
        messages = MessagesMessage.objects.filter(Q(recipient_id=request.user.id) & Q(sender_id=pk) | Q(sender_id = request.user.id) & Q(recipient_id=pk))
        # all_messages=MessageFilter(request.user.id,queryset=all_messages)
        sender = MessagesMessage.objects.filter(Q(recipient_id=request.user.id) | Q(sender_id = request.user.id)).values('sender_id','recipient_id')
        # sender = []
        # messages = []
        # for a_m in all_messages:
        #     if a_m.recipient_id == request.user.id or a_m.sender_id == request.user.id:
        #         sender.append(a_m.sender_id)
        #         messages.append(a_m)
        sender = User.objects.filter(Q(id__in = sender.values('sender_id'))|Q(id__in = sender.values('recipient_id'))).order_by('-id')
        # messages = MessagesMessage.objects.filter(recipient_id=request.user.id,sender_id=pk)

        return render(request, 'messanger/messanger.html' , {'messages':messages,'sender':sender,'pk':pk,})
