from minus.models import DjangobbForumPost
from minusstore.models import MinusstoreMinusweekstats,MinusstoreMinusrecord
from user.models import Userprofile,UsersUserrating

def top_minus_per_all_time():


	top_minus_per_all_time = []


	minus_record = MinusstoreMinusrecord.objects.order_by('-rating_score')[:10]

	for i in minus_record:
		top_minus_per_all_time.append(i)

	return top_minus_per_all_time


def top_minus_per_week():

    minus_week_stats = MinusstoreMinusweekstats.objects.order_by('-rate')[:10]
    mwk = []
    for i in minus_week_stats:
        mwk.append(i.minus_id)



    top_minus_per_week=MinusstoreMinusrecord.objects.filter(pk__in = mwk)

    return top_minus_per_week


def top_users():

	users = UsersUserrating.objects.order_by('-rating')[:10]



	return users




def last_forum():

	post = DjangobbForumPost.objects.order_by('-id')[:4]

	for i in post:
		# i.user =  AuthUser.objects.get(pk= i.user_id)
		i.body = i.body[:250] + '...'


	return post
