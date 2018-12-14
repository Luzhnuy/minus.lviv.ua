import datetime
from django.core.mail import send_mail
from minus.celery import app
# from django.contrib.auth.models import User
from minus.models import DeliverySubscriber
from minusstore.models import  MinusstoreMinusrecord
from celery.task.schedules import crontab
from celery.decorators import periodic_task





@app.task
def minus_send_new():
    m = []
    minuses = list(MinusstoreMinusrecord.objects.all().filter(pub_date__gte= datetime.datetime.now() - datetime.timedelta(days=7)))
    # (date_now[6:10],now[6:10]),
    # pub_date__month__range=(date_now[3:5],now[3:5]), pub_date__day__range=(date_now[0:2],now[0:2])))
    for i in minuses:
        m.append(i.title)
        # print('ye')

    print(m)
    m = ','.join(m)
    send_mail('celery','Доброго дня! Шановний користувач.За останій тиждень добавились такі мінусовки' + m,'minuslviv@gmail.com',['turupuru8@gmail.com'])












#
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
    # sender.add_periodic_task(10.0, minus_send_new.s(), name='add every 10')

    # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)
    #
    # # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
