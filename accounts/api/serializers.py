from rest_framework import serializers
from ..models import Account

class CreateAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('token',)

class ListAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('id', 'token',)