from django.urls import path
from .views import *

urlpatterns = [
    path('get_table_data/' , GatherAll.as_view()),
    path('point_to_point/' , PointtoPoint.as_view()),
    path('exports/'        , Export_endpoint.as_view()),
    path('imports/'        , Import_endpoint.as_view()),
    path('raw/'            , RawResource.as_view()),
    path('commodity_total/', Commodity_total.as_view()),
    path('ratio_ie/'       , Ratio_ie.as_view()),
]


