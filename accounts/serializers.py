from rest_framework import serializers
from .models import FundeeUser, FunderUser

class FunderUserSerializer(serializers.ModelSerializer):

	class Meta:
		fields = '__all__'
		model = FunderUser  


class FundeeUserSerializer(serializers.ModelSerializer):

	class Meta:
		fields = ['company_or_individual_name', 'account_number', 'email', 'bvn', 'company_or_individual_image', 'Id_or_CAC_verification']
		
		model = FundeeUser  