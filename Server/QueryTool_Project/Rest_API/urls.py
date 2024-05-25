from django.urls import path
from .views import *

urlpatterns = [
    path('all/'            ,  GatherAll.as_view()),
    path('ptop/'           , PointtoPoint.as_view()),
    path('exports/'        , Exports.as_view()),
    path('imports/'        , Imports.as_view()),
    path('raw/'            , RawResource.as_view()),
    path('commodity_total/', Commodity_total.as_view()),
    path('ratio_ie/'       , Ratio_ie.as_view()),
]

#path('table/'     , TablePayLoad.as_view()),
#path('query/'     , QueryLoader.as_view()),
#path('coldata/'   , TableDescripter.as_view()),
#path('table/<str:table_id>/', GetTableA.as_view()),

#path('table/data/', GetTable.as_view()),

#    path('', views.getData),
#    path('help/', views.getHelp),
#    path('help/commodity/', views.getCommodities),
#    path('column/', views.getColumnName)

