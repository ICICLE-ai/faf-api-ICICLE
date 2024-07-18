from django.urls import path
from .views import *

urlpatterns = [
    path('get_table_data/'   , GatherAll.as_view()),
    path('point_to_point/'   , PointtoPoint.as_view()),
    path('domestic_exports/' , Export_endpoint.as_view()),
    path('domestic_imports/' , Import_endpoint.as_view()),
    path('import_export_sum/', RawResource.as_view()),
    path('commodity_total/'  , Commodity_total.as_view()),
    #path('exports/', ExportEndpoint.as_view()),
]
