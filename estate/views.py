from django.shortcuts import render,redirect
from .models import Property
# Create your views here.

def get_add_property(req):
    return render(req,'add_property.html')

def get_update_property(req,ID):
    property=Property.objects.get(id=ID)
    context={
        "property":property
    }
    return render(req,"update_property.html",context=context)

def post_update_property(req,ID):
    property_name=req.POST["property_name"]
    price=req.POST["price"]
    property_detail=req.POST["property_detail"]
    
    property=Property.objects.get(id=ID)
    
    property.property_name=property_name
    property.price=price
    property.property_detail=property_detail

    property.save()

    return redirect("estates_home")

def delete_property(req,ID):
    property=Property.objects.get(id=ID)
    property.delete()
    return redirect("estates_home")

def post_add_property(req):
    property_name=req.POST["property_name"]
    price=req.POST["price"]
    property_detail=req.POST["property_detail"]

    new_property=Property(property_name=property_name,price=price,property_detail=property_detail)
    new_property.save()

    return redirect('estates_home')

def get_estates_home(req):
    all_estates=Property.objects.all()
    context={
        "estates":all_estates
    }
    return render(req,'estates_home.html',context=context)

