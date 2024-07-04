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
    path('profile/',views.profile, name="profile"),
    path('competences/developer/<int:developer_id>/', views.get_competence_by_dev, name='get_competence_by_dev'),
    path('competences/', views.get_all_competence, name='get_all_competence'),
]