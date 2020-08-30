from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view.as_view(), name = 'home'),
    path('api-getList/', views.getList, name='get-list'),
    path('api-total/<int:pk>/', views.getTotal,name='get-total'),
    path('api-twonumber/<int:num1>/<int:num2>/', views.postTwoNumber, name='add2number')
]