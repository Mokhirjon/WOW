from django.shortcuts import render
from rest_framework import generics
from .serializers import Customsirealizers
from .models import Customuser

# Create your views here.
class CreateCustomApieview(generics.CreateAPIView):
    queryset = Customuser.objects.all()
    serializer_class = Customsirealizers

class  DeleteCustomApieview(generics.DestroyAPIView):
    queryset = Customuser.objects.all()
    serializer_class = Customsirealizers