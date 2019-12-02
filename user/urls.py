from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_view
from rest_framework import routers
from . import views






urlpatterns = [
	url(r'^user/(?P<pk>[0-9]+)/$',views.user_page, name="user_page"),
	url(r'^reg/', views.RegisterFormView.as_view(), name="registration_page"),
	url(r'^login/', views.UserLoginView.as_view(), name="signin"),
	url(r'^update-profile/(?P<pk>[0-9]+)/$', views.ProfileUpdate.as_view(), name="profile_update"),
	url(r'^logout/', views.logout_view, name="logout"),
	url(r'^userlist/', views.userlist, name="userlist"),
	url(r'^userminuses/(?P<user_id>[0-9]+)/$', views.userminuses, name="userminuses"),
	url(r'^user-goods/(?P<user_id>[0-9]+)/$', views.user_goods, name="user_goods"),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
	url(r'^search/$',views.user_search,name="user_search"),
	url(r'^activities/$',views.activities,name="activities"),
	url(r'^false_auth/$',views.false_auth,name="false_auth"),
	url(r'^moderator-messages/$', views.moderator_messages,name="moderator_messages"),
	url(r'^add_moderator_message/(?P<object_pk>[0-9]+)/(?P<content_id>[0-9]+)/$',views.add_moderator_message,name="add_moderator_message"),
	url(r'get_user/(?P<pk>[0-9]+)/$', views.GetUser.as_view(),name="GetUser"),
	url(r'friend_request/(?P<to_user_id>[0-9]+)/$',views.FriendsRequest.as_view(),name="friend_request"),
	url(r'user-friends-requests/$',views.friends_requests,name="user_friend_request"),
	# url(r'list-freinds-request/$',views.list_friends_request, name="list-friends-request"),
	url(r'^all-friends/(?P<pk>[0-9]+)/$',views.all_friends, name="all_friends"),
	url(r'^user-advertisement/$',views.advertisement , name="advertisement"),
	url(r'^delete-selected-blurbs/(?P<pk>[0-9]+)/$',views.delete_selected_blurbs , name="delete-selected-blurbs"),
	url(r'^add-photo/$', views.AddPhoto.as_view(), name="add_photo"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
