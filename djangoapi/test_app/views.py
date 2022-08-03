from django.shortcuts import render
#import the types of responses u woul work with
from django.http import JsonResponse, response

# Create your views here.
# Views Handle Logic
#View Structure
#function to take request
def simple(request):
    #perform operations
    #a = 112+8
    #return response.HttpResponse(f"<h1>{a}</h1>")
    #return JsonResponse({"Answer": a})
    #Return HTTP or JSON Response
    #Testing Methods
    method = request.method.lower()
    if method == "get":
        return JsonResponse({"data": [1, 2, 3, 4, 5]})
    elif method == "post":
        return JsonResponse({"data": "data submitted"})
    elif method == "put":
        return JsonResponse({"data": "data updated"})
    return JsonResponse({"method": request.method})



