from .models import MinusstoreMinusauthor
from rest_framework import serializers


class MinusAuthorSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = MinusstoreMinusauthor
		fields = ('name','id')