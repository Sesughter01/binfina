from django.urls import path 
from . import views
urlpatterns = [
 	path('fundee-create/', views.create_user_Fundee),
]