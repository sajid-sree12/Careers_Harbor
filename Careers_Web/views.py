from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def loginView(request):
    return render(request,"login.html")

def aboutView(request):
    return render(request,"about.html")