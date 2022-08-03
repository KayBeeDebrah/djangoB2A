from django.shortcuts import render

#import the types of responses u woul work with
from django.http import JsonResponse, response
from rest_framework.views import APIView

# Create your views here.
#ClassBased Views

#Create Class

class simple(APIView):

    def post(self, request):
        return JsonResponse({"data": "Data Saved"})

    def get(self, request):
        return JsonResponse({"data": [3, 2,  1]})



