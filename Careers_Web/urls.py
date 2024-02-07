from django.urls import path
from Careers_Web import views

urlpatterns=[
    path('',views.home,name="home"),
    path('Login',views.loginView,name="Login"),
    path('about',views.aboutView,name= "About"),
    path('contact',views.contactView,name="contact"),
    path('user',views.userView,name="user"),
    path('admin_panel',views.adminView,name="adminV"),
]