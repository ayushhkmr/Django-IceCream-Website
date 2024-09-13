from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable':"this is sent",
        'variable1':"this is sent"
    }
    return render(request,'index.html',context)
# return HttpResponse("Welcome back to the home")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("Welcome back to the about page")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("Welcome back to the services page")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        phone=request.POST.get('phone')
        contact = Contact (name=name, email=email,phone=phone,desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "message sent.")
    return render(request,'contact.html')
    # return HttpResponse("Welcome back to the contact page")

