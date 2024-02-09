from django.urls import path
from Careers_Web import views

urlpatterns=[
    path('',views.home,name="home"),
    path('Login',views.loginView,name="Login"),
    path('User',views.User_views,name='User'),
    path('contact',views.contactView,name="contact"),
    path('user',views.userView,name="user"),
    path('AdminPanel',views.admin_views,name='AdminPanel'),
    path('approved/<int:pk>',views.feedback_approval,name='approved'),
    path('logout',views.logout_views,name='logout'),
]