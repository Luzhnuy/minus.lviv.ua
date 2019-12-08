from rest_framework import serializers
from minus.models import MessagesMessage
from django.contrib.auth.models import User


class MessagesSerializer (serializers.HyperlinkedModelSerializer):
    sender = serializers.JSONField()
    recipient = serializers.JSONField()

    class Meta:
        model = MessagesMessage
        fields = ["body", "sent_at", "read_at", "sender", "recipient"]