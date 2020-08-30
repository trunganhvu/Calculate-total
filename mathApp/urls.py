from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name = 'home'),
    path('api-getList/', views.getList, name='get-list'),
    path('api-total/<int:pk>/', views.getTotal,name='get-total'),
    path('api-twonumber/<int:num1>/<int:num2>/', views.addTwoNumber, name='add2number')
]