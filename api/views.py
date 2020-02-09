from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from estate.models import Property

import json

@csrf_exempt
def view_get_post_estate(req):

    if req.method=="GET":
        db_estates=Property.objects.all()
        all_estates=list(db_estates.values())
        print(all_estates)
        return JsonResponse({
            "properties":all_estates
        })

    elif req.method=="POST":
        body=json.loads(req.body)
        current_estate=Property.objects.create(property_name=body['property_name'],price=body['property_price'],property_detail=body['property_detail'])
        current_estate.save()
        return JsonResponse({
            "message":"Property Created",
            "property":{
                "id":current_estate.id,
                "property_name":current_estate.property_name,
                "property_detail":current_estate.property_detail,
                "property_price":current_estate.price
            }
        })

@csrf_exempt
def view_getByID_updateByID_deleteByID(req,ID):
    current_estate=Property.objects.get(id=ID)
    if req.method=="GET":
        return JsonResponse({
            "property":{
                "id":current_estate.id,
                "property_name":current_estate.property_name,
                "property_detail":current_estate.property_detail,
                "property_price":current_estate.price
            }
        })

    elif req.method=="PUT":
        body=json.loads(req.body)
        current_estate.property_name=body['property_name']
        current_estate.property_detail=body['property_detail']
        current_estate.property_price=body['property_price']

        current_estate.save()

        return JsonResponse({
            "message":"Updated Property",
            "property":{
                "id":current_estate.id,
                "property_name":current_estate.property_name,
                "property_detail":current_estate.property_detail,
                "property_price":current_estate.price
            }
        })

    elif req.method=="DELETE":
        current_estate.delete()

        return JsonResponse({
            "message":"Property Deleted",
            "property":{
                "id":current_estate.id,
                "property_name":current_estate.property_name,
                "property_detail":current_estate.property_detail,
                "property_price":current_estate.price
            }
        })


def pagination(req,pageNo,items):
    start=(pageNo-1)*items
    end=start+items

    if req.method=="GET":
        db_estates=Property.objects.all()
        all_estates=list(db_estates.values())
        print(all_estates[start:end])
        return JsonResponse({
            "parlors":all_estates[start:end]
        })


