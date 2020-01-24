from django.shortcuts import render,redirect
from .models import Property
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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

def search(req):
    return render(req, 'searchforms.html')

def searchdata(req):
    property_multiples = Property.objects.filter(property_name= req.GET['name']) 
    print("The searched data" , property_multiples)
    return HttpResponse("record searched")



def signup_part(req):
    if req.method == 'GET':
        return render(req, 'signUp.html')

    else:
        print(req.POST)
        user = User.objects.create_user(username=req.POST['input_Username'], password=req.POST['input_Password'], email=req.POST['input_Email'])
        print(user)
        user.save()
        return HttpResponse("Signup Successful")




def login_part(req):
    if req.method == 'GET':
        return render(req, 'login.html')

    else:
        print(req.POST)
        user = authenticate(username = req.POST['input_Username'], password = req.POST['input_Password'])
        print(user)
        if user is not None:
            login(req, user)
            return HttpResponse('login successful')

        else:
            return HttpResponse('invalid crenditals')
