
from django.urls import path
from . import views

urlpatterns = [
    path('contactus_employees/', views.create_employee, name='create_employee'),
    path('contactus_get/', views.read_employee, name='read_employee'),
    path('contactus_get_pk/<int:pk>/', views.read_employee_pk, name='read_employee_pk'),
    path('contactus_update_pk/<int:pk>/', views.update_employee, name='update_employee'),
    path('contactus_delete_pk/<int:pk>/', views.delete_employee, name='delete_employee'),
]