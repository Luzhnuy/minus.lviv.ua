from django.shortcuts import render
from minus.models import MessagesMessage
from django.contrib.auth.models import User
from django.db.models import Q
from messanger.models import NewMessagesChannels
from user.filter import UserFilter
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

def users_search(request):
    users_all = User.objects.all()
    print('0122222222222222222233333333333333333333333333333333')
    print(request.GET)
    print('saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    # users = UserFilter(request.GET, queryset=users_all)
    users = User.objects.filter(Q(first_name__startswith=request.GET['search']) | Q(last_name__startswith=request.GET['search'])| Q(username__startswith=request.GET['search'])| Q(email__startswith=request.GET['search']))
    print('---------------------------------------------')
    print(users)
    print('-----------------------------------------')
    # users = users.qs
    print('gello')
    print(users)
    sender = MessagesMessage.objects.filter(Q(recipient_id=request.user.id) | Q(sender_id = request.user.id),Q(recipient_id__in=users.values_list('id')) | Q(sender_id__in = users.values_list('id'))).values('sender_id','recipient_id')
    sender = User.objects.filter(Q(id__in = sender.values('sender_id'))|Q(id__in = sender.values('recipient_id'))).order_by('-id')
    for i in sender:
        i.new = NewMessagesChannels.objects.filter(frm_user = i.id)
        # print(i.new)
        # print('messanger sender if exist new')

    print('-00-------------00000000000000000000000000')
    print(sender)
    print('0000000000000000000000000000000000000000000')
    return render(request, 'messanger/messanger.html' , {'sender':sender,})
