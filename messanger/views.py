from django.shortcuts import render
from minus.models import MessagesMessage
from django.contrib.auth.models import User
from django.db.models import Q
from messanger.models import NewMessagesChannels
# from messanger.filters import MessageFilter

# Create your views here.

def messanger(request):
    if request.user.is_authenticated:
        sender = MessagesMessage.objects.filter(Q(recipient_id=request.user.id) | Q(sender_id = request.user.id)).values('sender_id','recipient_id')
        sender = User.objects.filter(Q(id__in = sender.values('sender_id'))|Q(id__in = sender.values('recipient_id'))).order_by('-id')
        for i in sender:
            i.new = NewMessagesChannels.objects.filter(frm_user = i.id)
            print(i.new)
            print('messanger sender if exist new')
        return render(request, 'messanger/messanger.html' , {'sender':sender,})



def messages(request,pk):
    if request.user.is_authenticated:
        messages = MessagesMessage.objects.filter(Q(recipient_id=request.user.id) & Q(sender_id=pk) | Q(sender_id = request.user.id) & Q(recipient_id=pk))
        sender = MessagesMessage.objects.filter(Q(recipient_id=request.user.id) | Q(sender_id = request.user.id)).values('sender_id','recipient_id')
        try:
            NewMessagesChannels.objects.get(frm_user=pk).delete()
        except NewMessagesChannels.DoesNotExist:
            print('Newmessages does not exist')
        sender = User.objects.filter(Q(id__in = sender.values('sender_id'))|Q(id__in = sender.values('recipient_id'))).order_by('-id')
        for i in sender:
            i.new = NewMessagesChannels.objects.filter(frm_user = i.id)
            print(i.new)
            print('messanger sender if exist new')
        return render(request, 'messanger/messanger.html' , {'messages':messages,'sender':sender,'pk':pk,})
