from django.urls import path
from .views import TablePayLoad, QueryLoader, TableDescripter

urlpatterns = [
    path('table/'  , TablePayLoad.as_view()),
    path('query/'  , QueryLoader.as_view()),
    path('coldata/', TableDescripter.as_view()),
#    path('', views.getData),
#    path('help/', views.getHelp),
#    path('help/commodity/', views.getCommodities),
#    path('column/', views.getColumnName)
]
