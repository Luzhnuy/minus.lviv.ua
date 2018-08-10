from django.conf.urls import url,include

from . import views

urlpatterns = [
	url(r'^shame/', views.desk_of_shame, name="desk_of_shame"),
]