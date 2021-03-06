from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from messanger import consumers



#
# websocket_urlpatterns = [
#     url(r'^ws/messanger/(?P<pk>[0-9]+)/$', consumers.ChatConsumer),
# ]

application = ProtocolTypeRouter({
     "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^(?P<pk>[0-9]+)/$", consumers.LiveuserConsumer),
            # url(r"None/", consumers.LiveuserConsumer),
            url(r'^messanger/(?P<pk>[0-9]+)/$', consumers.MessangerConsumer),
        ])
    ),
})
