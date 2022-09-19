from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('AgregarEdificios', views.AgregarEdificios, name='AgregarEdificios'),
    path('Sedes',views.sedes, name='Sedes'),
]
