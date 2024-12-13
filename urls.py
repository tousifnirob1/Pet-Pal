from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html/', views.index, name='index'),
    path('index.html/topics-detail.html/', views.index, name='index'),
    path('topics-detail.html/', views.topics_detail, name='topics-detail'),
    path('giver-details.html/', views.giver_details, name='giver-details'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('add_pet/', views.add_pet, name='add_pet'),
    path('add_caregiver/', views.add_caregiver, name='add_caregiver'),
]
