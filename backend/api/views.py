from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# User Model View for admin access only
class UserView(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser]
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	lookup_field = 'uid'
	filter_fields = ['first_name','last_name','email','phone','date_of_birth','address','role','is_approved','is_active','is_superuser','created_on']
	filterset_fields = ['first_name','last_name','email','phone','date_of_birth','address','role','is_approved','is_active','is_superuser','created_on']
	search_fields = ['first_name','last_name','email','phone','date_of_birth','address','role','is_approved','is_active','is_superuser','created_on']
	ordering_fields = ['first_name','last_name','email','phone','date_of_birth','address','role','is_approved','is_active','is_superuser','created_on']