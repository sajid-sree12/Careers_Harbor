from django.shortcuts import render
from careers_web.models import Career_feedback
# Create your views here.

def home(request):
    career_records=Careers_hub.objects.all()
    feedback_records=Career_feedback.objects.filter(status="Approved")
    context={'feedback_records':feedback_records,'career_records':career_records}
    if request.method=="POST":
        f_name=request.POST.get('f_name')
        f_email=request.POST.get('f_email')
        f_rating=int(request.POST.get('f_rating'))
        feedback=request.POST.get('feedback')
        obj=Career_feedback(fullname=f_name,email=f_email,rating=f_rating,feedback=feedback)
        obj.save()
        messages.info(request,'Feedback inserted successfully')
        return render(request,'index.html',context)

    return render(request,'index.html',context)


def login_views(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are alredy Logged in...")
        if request.user.is_superuser:
            return redirect('AdminPanel')
        else:
            return redirect('User')
    if request.method=='POST':
        userName=request.POST.get('username')
        passWord=request.POST.get('password')
        user=authenticate(username=userName,password=passWord,is_activate=True)
        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                messages.success(request,'Admin  you are successfully logged in..')
                return redirect('AdminPanel')
            else:
                messages.info(request,'normal user successfully login')
                return redirect('User')
        else:
            messages.warning(request,'You enter wrong user or password')
            return redirect('login')
    return render(request,'error.html')

def aboutView(request):
    return render(request,"about.html")

def contactView(request):
    return render(request,"contact.html")

def adminView(request):
    return render(request,"admin.html")

def userView(request):
    return render(request,"user.html")