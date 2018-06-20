from minus.models import MinusstoreMinusweekstats, MinusstoreMinusrecord,UsersUserrating,AuthUser

def top_minus_per_all_time():
	
	
	top_minus_per_all_time = []
	
	# top_minus_id = []
	
	# for i in range(10):	
	# 	top_minus_id.append(minus[i].rate)
	
	# for i in top_minus_id:
	minus_record = MinusstoreMinusrecord.objects.order_by('-rating_score')[:10]
	
	for i in minus_record:
		top_minus_per_all_time.append(i)

	return top_minus_per_all_time


def top_minus_per_week():

	top_minus_per_week = []	

	minus_week_stats = MinusstoreMinusweekstats.objects.order_by('-rate')[:10]

	

	for i in minus_week_stats:
		top_minus_per_week.append(MinusstoreMinusrecord.objects.get(pk = i.minus_id))


	return top_minus_per_week


def top_users():

	
	top_users = []
	
	# top_minus_id = []
	
	# for i in range(10):	
	# 	top_minus_id.append(minus[i].rate)
	
	# for i in top_minus_id:
	users = UsersUserrating.objects.order_by('-rating')[:10]
	
	for i in users:
		top_users.append(AuthUser.objects.get(pk = i.user_id))

	return top_users
