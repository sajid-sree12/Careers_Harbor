from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def loginView(request):
    return render(request,"login.html")

def aboutView(request):
    return render(request,"about.html")

def contactView(request):
    return render(request,"contact.html")

def adminView(request):
    return render(request,"admin.html")

def userView(request):
    return render(request,"user.html")