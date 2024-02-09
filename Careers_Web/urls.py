from django.urls import path
from Careers_Web import views

urlpatterns=[
    path('',views.home,name="home"),
    path('Login',views.login_views,name="login"),
    path('contact',views.contactView,name="contact"),
    path('user',views.userView,name="user"),
    path("about",views.aboutView, name="About"),
    path('feedback',views.feedback_view,name='feedback'),
    path('AdminPanel',views.admin_views,name='AdminPanel'),
    path('approved/<int:pk>',views.feedback_approval,name='approved'),
    path('delete/<int:pk>',views.feedback_delete,name='delete'),
    path('logout',views.logout_views,name='logout'),
]