from django.db import models

# Create your models here.
class Business(models.Model):
	name_of_business = models.CharField(max_length=250, blank=False, unique=True)
	Business_desc = models.CharField(max_length=500, blank=False)
	campaign_start = models.DateField()
	campaign_end = models.DateField()
	images = models.ImageField(blank=True)