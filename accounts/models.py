from django.db import models
from django.contrib.auth.models import AbstractUser


class FundeeUser(AbstractUser):
	company_or_individual_name = models.CharField(max_length=50, null=True, blank=False, unique=True)
	account_number = models.CharField(max_length=10)
	email = models.EmailField(('email address'), unique = True)
	bvn = models.CharField(max_length=11)
	company_or_individual_image = models.ImageField(null=True)
	Id_or_CAC_verification = models.ImageField(null=False)

	def __str__(self):
		return self.email
	



class FunderUser(models.Model):
	investors_name = models.CharField(max_length=50, null=True, blank=True, unique=True)
	email = models.EmailField(('email address'), unique=True)
	investors_image = models.ImageField(null=True)
	next_of_kin = models.CharField(max_length=50, null=True, blank=True)


	def __str__(self):
		return self.investors_name
