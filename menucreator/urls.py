from django.urls import path

from menucreator import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wordpress/<int:menu_id>/', views.wordpress, name='wordpress')
]
