from rest_framework import serializers
from .models import FundeeUser, FunderUser

class FunderUserSerializer(serializers.ModelSerializer):

	class Meta:
		fields = '__all__'
		model = FunderUser  


class FundeeUserSerializer(serializers.ModelSerializer):

	class Meta:
		fields = '__all__'
		model = FundeeUser  