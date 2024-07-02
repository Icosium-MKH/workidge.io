from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.register, name="register"),
    path('register/developer/', views.developer_registration, name='developer_registration'),
    path('register/recruiter/', views.recruiter_registration, name='recruiter_registration'),    
    path('login/',views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('offers/',views.offers, name="offers"),
]