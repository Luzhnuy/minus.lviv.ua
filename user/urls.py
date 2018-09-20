from django.conf.urls import url,include

from . import views

urlpatterns = [
	url(r'^$',views.user_page, name="user_page"),
	url(r'^reg/', views.registration_page, name="registration_page"),
	url(r'^login/', views.signin, name="signin")
]
