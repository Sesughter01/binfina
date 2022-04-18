from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import FundeeUserSerializer, FunderUserSerializer
from drf_yasg.utils import swagger_auto_schema 

from .models import FundeeUser, FunderUser
# Create your views here.
@swagger_auto_schema(methods=["POST"], request_body=FundeeUserSerializer())
@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def create_user_Fundee(request):
    user = request.user
    serializer = FundeeUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
   
                                                         
    return Response(serializer.data, status=status.HTTP_201_CREATED)