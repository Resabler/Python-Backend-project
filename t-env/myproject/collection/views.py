from rest_framework.pagination import PageNumberPagination
class Custompagination(PageNumberPagination):
    page=10
    custom_page_size = 'page'  
    max_page_size = 100 


from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response



class Listcreate(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    pagination_class=Custompagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]  
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'role']

   


class  Retrieveupdatedelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id' 
    pagination_class=Custompagination
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]