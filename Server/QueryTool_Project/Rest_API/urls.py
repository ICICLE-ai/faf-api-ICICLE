from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('query/', views.getQuery),
    path('column/', views.getColumnName)
]
