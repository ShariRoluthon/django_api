from django.urls import path
from .import views

urlpatterns = [
    path('',views.Apioverview),
    path('emplist/',views.EmpList,name='emplist'),
]