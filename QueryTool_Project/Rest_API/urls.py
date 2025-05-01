from django.urls import path
from .views import *

urlpatterns = [
    path('get_table_data/'   , GatherAll.as_view()),
    path('point_to_point/'   , PointtoPoint.as_view()),
    path('exports_imports_details/' , Export_endpoint.as_view()),
    # path('imports/' , Import_endpoint.as_view()),
    path('import_export_sum/', RawResource.as_view()),
    path('commodity_total/'  , Commodity_total.as_view()),
    path('data_option/'       , Data_Option.as_view()),

    path('exports_imports_mode_details/', Export_Mode_Details.as_view()),
    # path('get_export_commodity_Details/', Export_Commodity_Details.as_view()),

    path('get_bar_chart_details/', Bar_Chart_Details.as_view()),
    # path('get_export_commodity_Details/', Export_Commodity_Details.as_view()),

    path('get_domestic_flow_details/', Domestic_Flow_Tab.as_view()),
    # path('get_domestic_expoer_tab/', Domestic_Flow_Tab.as_view()),

    path('get_foreign_import_details/', Foreign_Import_Tab.as_view()),
    # path('get_foreign_import_tab/', Foreign_Import_Tab.as_view()),

    path('get_foreign_export_details/', Foreign_Export_Tab.as_view()),
    # path('get_foreign_export_tab/', Foreign_Export_Tab.as_view()),
]
