from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is homepage")

def about(request):
    #return HttpResponse("The about page is under construction.")
    return render(request, "about.html")
def services(request):
    #return HttpResponse("The servies page is under construction.")
    return render(request, "services.html")

def contact(request):
    #return HttpResponse("The contact page is under construction. For further queries please contact to: +977 9847103602 or +977 9861217046")
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request,"Your form has been submitted.")
    return render(request, "contact.html")
    