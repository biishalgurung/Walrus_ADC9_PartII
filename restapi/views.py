from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from estate.models import Property
import json

@csrf_exempt
def view_get_post_property(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
        property = Property.objects.all()
        print("QuerySet objects => ",property)
        list_of_property = list(property.values("property_name","price","property_detail", "uploaded_at"))
        print("List of property objects => ",list_of_property)
        dictionary_name = {
        "property":list_of_property
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['property_name'])
        print(python_dictionary_object['price'])
        print(python_dictionary_object['property_detail'])
        print(python_dictionary_object['uploaded_at'])
        Property.objects.create(property_name=python_dictionary_object['property_name'],price=python_dictionary_object['price'],property_detail=python_dictionary_object['property_detail'],uploaded_at=python_dictionary_object['uploaded_at'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        property = Property.objects.get(id = ID)
        print(type(property.property_name))
        return JsonResponse({
            "id":property.id,
            "property_name":property.property_name,
            "price":property.price,
            "property_detail":property.property_detail,
            "uploaded_at":property.uploaded_at
        })
    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        })