from django.shortcuts import render

#import the types of responses u woul work with
from django.http import JsonResponse, response
from rest_framework.views import APIView
#import Model
from .models import TestModel, RegionModel
from .serializers import SimpleSerializer
from django.forms.models import model_to_dict

# Create your views here.
#ClassBased Views

#Create Class

class Simple(APIView):

    def post(self, request):
        # validating with serializers
        serializer = SimpleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_Region_content = RegionModel.objects.create(
                 Region_ID=request.data["Region_ID"],
                 Region_Name=request.data["Region_Name"]
         )
        #print(new_Region_content)
        #In place of manually specifying dict/list Serializer automatically converts our data
        return JsonResponse({"data": SimpleSerializer(new_Region_content).data})

    def get(self, request):
        #using object manager to filter data from the models
        #declare variable content to handle data from the model
        content = RegionModel.objects.all()
        # Serializer automatically converts our data. MANY=TRUE  signifies that we expct more than one object
        return JsonResponse({"data": SimpleSerializer(content, many=True).data})



