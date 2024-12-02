from django.urls import path
from .views import *

urlpatterns = [
    path('get_table_data/'   , GatherAll.as_view()),
    path('point_to_point/'   , PointtoPoint.as_view()),
    path('domestic_exports/' , Export_endpoint.as_view()),
    path('domestic_imports/' , Import_endpoint.as_view()),
    path('import_export_sum/', RawResource.as_view()),
    path('commodity_total/'  , Commodity_total.as_view()),
    path('data_option/'       , Data_Option.as_view()),
    #path('exports/', ExportEndpoint.as_view()),
    path('get_transpotation/', Transpotation_Details.as_view()),
    # path('get_transpotation/', Transpotation_details.as_view()),

    path('get_commodity/', Commodity_Details.as_view()),
    # path('get_transpotation/', Transpotation_details.as_view()),

    path('get_domestic_origin/', Domestic_Origin.as_view()),
    # path('get_transpotation/', Transpotation_details.as_view()),

    path('get_domestic_destination/', Domestic_Destination.as_view()),
    # path('get_transpotation/', Transpotation_details.as_view()),

    path('get_export_mode_Details/', Export_Mode_Details.as_view()),
    # path('get_export_commodity_Details/', Export_Commodity_Details.as_view()),

    path('get_bar_chart_Details/', Bar_Chart_Details.as_view()),
    # path('get_export_commodity_Details/', Export_Commodity_Details.as_view()),
]
