from django.shortcuts import render

#import the types of responses u woul work with
from django.http import JsonResponse, response
from rest_framework.views import APIView
#Implement ViewSets in Views to reduce number of code lines
from rest_framework import generics, viewsets
#import Model
from .models import TestModel, RegionModel
from .serializers import SimpleSerializer
from django.forms.models import model_to_dict

# Create your views here.
#ClassBased Views

#Create APIVIEW Class


#Create classes with Generics
#ModelViewset gives the abstraction all CRUD OPERATIONS
class SimpleViewset(viewsets.ModelViewSet):
    queryset = RegionModel.objects.all()
    serializer_class = SimpleSerializer

