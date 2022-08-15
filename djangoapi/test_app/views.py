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
        #calls the serializer create method
        serializer.save()
        #In place of manually specifying dict/list Serializer automatically converts our data
        return JsonResponse({"data": serializer.data})

    def get(self, request):
        #using object manager to filter data from the models
        #declare variable content to handle data from the model
        content = RegionModel.objects.all()
        # Serializer automatically converts our data. MANY=TRUE  signifies that we expct more than one object
        return JsonResponse({"data": SimpleSerializer(content, many=True).data})

    # *args holds Non-Keyword Arguments, **kwargs holds Keyword Arguments and values
    def put(self, request, *args, **kwargs):
    #validation (check if Region_ID keyword(Region_ID) does not exist)
        model_id = kwargs.get("Region_ID", None)
        #if it does not exist then return error message
        if not model_id:
            return JsonResponse({"error":"method /PUT/ not allowed"})

        try:
            #assign the existing values in db to to instance based on primary key
            instance = RegionModel.objects.get(Region_ID=model_id)
        except:
            #if error occurs display
            return JsonResponse({"error": "Object does not exist"})

        #pass new data and instance to the serializer
        serializer = SimpleSerializer(data=request.data, instance=instance)
        #validate the new data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})







