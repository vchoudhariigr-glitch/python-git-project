from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-member/', views.add_member, name='add_member'),
    path('members/', views.member_list, name='member_list'),
    path('add-trainer/', views.add_trainer, name='add_trainer'),
]