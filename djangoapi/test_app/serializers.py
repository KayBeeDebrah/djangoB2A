#import serialiser class
#Serializers convert data to list or dictionary depending on the
#structure of the data
from rest_framework import serializers

#Create the serializer class
class SimpleSerializer(serializers.Serializer):
    #Region_ID = serializers.CharField
    Region_ID = serializers.CharField()
    Region_Name = serializers.CharField()
    #Ignore Validation and Use field for conversion purposes only
    #Region_Name = serializers.CharField(read_only=True)




