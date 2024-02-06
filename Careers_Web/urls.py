from django.urls import path
from Careers_Web import views

urlpatterns=[
    path('',views.home,name="home"),
    path('Login',views.loginView,name="Login"),
    path('about',views.aboutView,name= "About"),
]