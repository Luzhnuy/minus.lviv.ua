from django.conf.urls import url,include
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
	url(r'^user/(?P<pk>[0-9]+)/$',views.user_page, name="user_page"),
	url(r'^reg/', views.RegisterFormView.as_view(), name="registration_page"),
	url(r'^login/', views.UserLoginView.as_view(), name="signin"),
	url(r'^logout/', views.logout_view, name="logout"),
	url(r'^userlist/', views.userlist, name="userlist"),
]
