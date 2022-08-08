from django.shortcuts import render

#import the types of responses u woul work with
from django.http import JsonResponse, response
from rest_framework.views import APIView
#import Model
from .models import TestModel, RegionModel
from django.forms.models import model_to_dict

# Create your views here.
#ClassBased Views

#Create Class

class simple(APIView):

    def post(self, request):
        new_Region_content = RegionModel.objects.create(
                 Region_ID=request.data["Region_ID"],
                 Region_Name=request.data["Region_Name"]
         )
        #print(new_Region_content)
        return JsonResponse({"data": model_to_dict(new_Region_content)})

    def get(self, request):
        #using object manager to filter data from the models
        #declare variable content to handle data from the model
        content = RegionModel.objects.all().values()
        return JsonResponse({"data": list(content)})



