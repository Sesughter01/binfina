from django.contrib import admin
from .models import FundeeUser, FunderUser
# Register your models here.

admin.site.register(FundeeUser)
admin.site.register(FunderUser)