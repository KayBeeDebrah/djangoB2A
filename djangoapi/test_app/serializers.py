#import serialiser class
#Serializers convert data to list or dictionary depending on the
#structure of the data
from rest_framework import serializers



class SimpleObject():
    #Declare an init method == Constructor
    def __init__(self, Region_Name):
        self.Region_Name = Region_Name

#Create the serializer class
class SimpleObjectSerializer(serializers.Serializer):
    #Region_ID = serializers.CharField
    Region_Name = serializers.CharField()

def run_data():
    #SimpleObject accepts the raw data and assigns to the corresponding fields
    simple_var = SimpleObject("Tema Motorway")
    #simpleobjectserializer ensures data meets criteria for data types
    simple_var_serializer = SimpleObjectSerializer(simple_var)

    #Data can be represented with the serilizer variable
    print(simple_var_serializer.data)


