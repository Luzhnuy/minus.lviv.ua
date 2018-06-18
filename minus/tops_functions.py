from minus.models import MinusstoreMinusstats, MinusstoreMinusrecord

def top_minus_per_all_time():
	minus = MinusstoreMinusstats.objects.all()
	top_minus_per_all_time = []
	top_minus_id = []
	for i in range(10):	
		top_minus_id.append(minus[i].minus_id)

	for i in top_minus_id:
		top_minus_per_all_time.append(MinusstoreMinusrecord.objects.get(pk = i))

	return top_minus_per_all_time		