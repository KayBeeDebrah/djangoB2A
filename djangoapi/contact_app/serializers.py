#import serialiser class
#Serializers convert data to list or dictionary depending on the
#structure of the data
from rest_framework import serializers
#import models
from .models import RegionModel, TestModel

#Create the serializer class using a ModelSerializer(NO definition of fileds, create and update methods)
class SimpleSerializer(serializers.ModelSerializer):

    class Meta:
# assign the model in question to a variable
        model = RegionModel
# Indicate fields to display
        #Display Specific Fields
        #fields = ("Region_ID", "Region_Name", )
        #Display all fields
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestModel
        fields = "__all__"













