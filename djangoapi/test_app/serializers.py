#import serialiser class
#Serializers convert data to list or dictionary depending on the
#structure of the data
from rest_framework import serializers
#import models
from .models import RegionModel

#Create the serializer class
class SimpleSerializer(serializers.Serializer):
    #Region_ID = serializers.CharField
    Region_ID = serializers.CharField()
    Region_Name = serializers.CharField()
    #Ignore Validation and Use field for conversion purposes only
    #Region_Name = serializers.CharField(read_only=True)

    #using the serializer to save
    def create(self, validated_data):
        return RegionModel.objects.create(**validated_data)

    # using the serializer to update
    def update(self, instance, validated_data):
        #filter the record with the id and update with the new validated data
        RegionModel.objects.filter(Region_ID=instance.Region_ID).update(**validated_data)
        #fetch the updated data based on the id
        return RegionModel.objects.get(Region_ID=instance.Region_ID)






