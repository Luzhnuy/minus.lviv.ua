from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from messanger import consumers

application = ProtocolTypeRouter({
     "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^front(end)/$", consumers.ChatConsumer),
        ])
    ),
})
