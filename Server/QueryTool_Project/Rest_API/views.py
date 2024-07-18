#Rest_API/views.py
from django.shortcuts import render
from django.http      import HttpResponse
import pandas as pd
from io import StringIO


from rest_framework.response   import Response
from rest_framework.decorators import api_view
from rest_framework.views      import APIView

#files
from src.Data_Lookup    import QueryTool
from src.GrabTable      import GrabTable
from src.PointToPoint   import PointToPoint
from src.Exports        import Exports
from src.Export   import Export
from src.Imports        import Imports
from src.CommodityTotal import CommodityTotal
import Rest_API.examples as e
import Rest_API.serializers as s

from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter
import logging
    
logger = logging.getLogger('Rest_API.views')

#useful functions
def readfile(file_path):
    with open(file_path, 'r') as fp:
        return fp.read()

###########################################################################################
class GatherAll(APIView):
    @extend_schema(
        description=readfile('Rest_API/endpoint_desc/get_table_data/desc.txt'),
        parameters=[
            OpenApiParameter(
                name='table',
                description=readfile('Rest_API/endpoint_desc/get_table_data/table.txt'),
            ),
            OpenApiParameter(
                name='timeframe',
                description=readfile('Rest_API/endpoint_desc/get_table_data/timeframe.txt'),
            ) 
        ],    
        examples=[
            OpenApiExample(
                'Example',
                value = e.tableModel_example,
                media_type="application/json",
            )
        ],
        request=s.TableSerializer()
    )
    def post(self, request):
        serializer = s.TableSerializer(data=request.data)
        if serializer.is_valid():
            table  = serializer.validated_data['table']
            timef  = serializer.validated_data['timeframe']
            gt   = GrabTable(table, timef)
            if gt.fail == 1: return Response("ERROR: Wrong Table")
            query = gt.setup()
             
            logger.info(f"Grab Table Query: {query}")
            
            lookup = QueryTool()
            data = lookup.query(query)
            try:
                csv_data = data.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = f'attachment; filename={request.data["table"]}.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)

###########################################################################################
class PointtoPoint(APIView):
    @extend_schema(
        description=readfile('Rest_API/endpoint_desc/point_to_point/desc.txt'),
        parameters=[
            OpenApiParameter(
                name='commodity',
                description=readfile('Rest_API/endpoint_desc/point_to_point/commodity.txt'),
            ),
            OpenApiParameter(
                name='origin',
                description=readfile('Rest_API/endpoint_desc/point_to_point/origin.txt'),
            ),           
            OpenApiParameter(
                name='destination',
                description=readfile('Rest_API/endpoint_desc/point_to_point/destination.txt'),
            ),           
            OpenApiParameter(
                name='timeframe',
                description=readfile('Rest_API/endpoint_desc/point_to_point/timeframe.txt'),
            ),           
        ], 
        examples=[
            OpenApiExample(
                'Year Range Example',
                value=e.PointToPointExample1,
                media_type="application/json",
            ),
            OpenApiExample(
                'Single Year Example',
                value=e.PointToPointExample2,
                media_type="application/json",
            ),
            OpenApiExample(
                'Response Example',
                value=e.PtoPReturnExample,
                media_type="application/json",
            )
        ],
        request=s.PointToPointSerializer(),
        responses={
            '200':s.PtoPReturnSerializer(many=True),
        },
    )

    def post(self, request):
        serializer = s.PointToPointSerializer(data=request.data)
        if serializer.is_valid():
            data = PointToPoint(
                serializer.validated_data['commodity'],
                serializer.validated_data['origin'],
                serializer.validated_data['destination'],
                serializer.validated_data['timeframe']
            )
            query = data.setup()
            if query == False: return Response("ERROR: Check data") 
            logger.info(f"PointToPoint: {query}")
            lookup = QueryTool()
            data = lookup.query(query)
            try:
                csv_data = data.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = 'attachment; filename=PointToPoint.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)

##########################################################################################
class Export_endpoint(APIView):
    @extend_schema(
        description=readfile('Rest_API/endpoint_desc/exports/desc.txt'),
        parameters=[
            OpenApiParameter(
                name='origin',
                description=readfile('Rest_API/endpoint_desc/exports/origin.txt'),
            ),
            OpenApiParameter(
                name='timeframe',
                description=readfile('Rest_API/endpoint_desc/exports/timeframe.txt'),
            ),
 
        ],
        examples=[
            OpenApiExample(
                'Single Year Example',
                value=e.exportSingleExample1,
                media_type="application/json",
            ), 
            OpenApiExample(
                'Year Window Example',
                value=e.exportMultiExample2,
                media_type="application/json",
            ),
           OpenApiExample(
                'Return Example',
                value=e.exportReturnExample,
                media_type="application/json",
            )

        ],
        request=s.ExportsSerializer(),
        responses={
            '200':s.ExportsReturnSerializer(many=True)
        },
    )

    def post(self, request):
        serializer = s.ExportsSerializer(data=request.data)
        if serializer.is_valid():
            data = Exports(
                serializer.validated_data['origin'],
                serializer.validated_data['timeframe']
            )
            query = data.setup()

            if query == False: return Response("Error: Check Data", 400)
            logger.info(f"Export Endpoint:{query}")
            lookup = QueryTool()
            data = lookup.query(query)
            try:
                csv_data = data.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = f'attachment; filename=exports_{serializer.validated_data["origin"]}.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)

 
##########################################################################################
class Import_endpoint(APIView):
    @extend_schema(
        description=readfile('Rest_API/endpoint_desc/imports/desc.txt'),
        parameters=[
            OpenApiParameter(
                name='origin',
                description=readfile('Rest_API/endpoint_desc/imports/origin.txt'),
            ),
            OpenApiParameter(
                name='timeframe',
                description=readfile('Rest_API/endpoint_desc/imports/timeframe.txt'),
            ),
 
        ],
 
        examples=[
            OpenApiExample(
                'Single Year Example',
                value=e.exportSingleExample1,
                media_type="application/json",
            ), 
            OpenApiExample(
                'Year Window Example',
                value=e.exportMultiExample2,
                media_type="application/json",
            ),
           OpenApiExample(
                'Return Example',
                value=e.importReturnExample,
                media_type="application/json",
            )

        ],
        request=s.ImportsSerializer(),
        responses={
            '200':s.ImportsReturnSerializer(many=True)
        }
    )

    def post(self, request):
        serializer = s.ImportsSerializer(data=request.data)
        if serializer.is_valid():
            data = Imports(
                serializer.validated_data['origin'],
                serializer.validated_data['timeframe']
            )
            query = data.setup()

            if query == False: return Response("Error: Check Data", 400)
            logger.info(f"Export Endpoint:{query}")
            lookup = QueryTool()
            data = lookup.query(query)
            try:
                csv_data = data.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = f'attachment; filename=Imports_{serializer.validated_data["origin"]}.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)


##########################################################################################
#fr_import
#fr_export
##########################################################################################
class RawResource(APIView):
    @extend_schema(
        description=readfile('Rest_API/endpoint_desc/import_export_sum/desc.txt'),
        parameters=[
            OpenApiParameter(
                name='origin',
                description=readfile('Rest_API/endpoint_desc/import_export_sum/origin.txt'),
            ),
            OpenApiParameter(
                name='timeframe',
                description=readfile('Rest_API/endpoint_desc/import_export_sum/timeframe.txt'),
            ),
 
        ],
        examples=[
            OpenApiExample(
                'Example Year',
                value=e.rawExample1,
                media_type="application/json",
            ), 
            OpenApiExample(
                'Example Year Frame',
                value=e.rawExample2,
                media_type="application/json",
            ),
            OpenApiExample(
                'Return Example',
                value=e.rawExampleReturn,
                media_type="application/json",
            ),
        ],
        request=s.RawResourceSerializer(),
        responses={
            '200':s.RawResourceReturnSerializer(many=True)
        }
    )
    def post(self, request):
        serializer = s.RawResourceSerializer(data=request.data)
        if serializer.is_valid():
            #Send data to class and return data as pandas framework
            gen_query = Imports(
                serializer.validated_data['origin'],
                serializer.validated_data['timeframe']
            )
 
            gen_query2 = Exports(
                serializer.validated_data['origin'],
                serializer.validated_data['timeframe']
            )
            
            #Add ton value based on column and commodity type
            query  = gen_query.setup()
            query2 = gen_query2.setup()
            logger.info(f"SumRaw:{query}\n{query2}")
            if query == False: return  Response("Error: Check Data", 400)
            if query2 == False: return Response("Error: Check Data2", 400)
            lookup = QueryTool()
            self.df1 = lookup.query(query)
            self.df2 = lookup.query(query2)
            commodities = lookup.query("SELECT description FROM c")["description"]
            
            #splitting proccess between 1 and 2, will join both dataframes in end
            output1 = {
                "origin"   : [],
                "commodity": [],
                "option":    [],
            }
            output2 = {
                "origin"   : [],
                "commodity": [],
                "option":    [],
            }
 
            for col  in self.df1:
                if col[:4] == 'tons':
                    output1[col] = []
                    for c in commodities:
                        if c not in output1['commodity']:
                            output1['origin'].append(serializer.validated_data['origin'])
                            output1['commodity'].append(c)
                            output1['option'].append("Imports")
                        output1[col].append(self._quickSum(1, c, col))
            for col  in self.df2:
                if col[:4] == 'tons':
                    output2[col] = []
                
                    for c in commodities:
                        if c not in output2['commodity']:
                            output2['origin'].append(serializer.validated_data['origin'])
                            output2['commodity'].append(c)
                            output2['option'].append("Exports")
                        output2[col].append(self._quickSum(0, c, col))
            
            new_df1 = pd.DataFrame(output1)
            new_df2 = pd.DataFrame(output2)
            #joined dataframe
            complete_df = pd.concat([new_df1, new_df2])
            try:
                csv_data = complete_df.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = f'attachment; filename=SumImportOutports{serializer.validated_data["origin"]}.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)



    def _quickSum(self, n, check, sumcol):
        if n: filtered_df = self.df1[self.df1['Commodity'] == check]
        else: filtered_df = self.df2[self.df2['Commodity'] == check]
        return filtered_df[sumcol].sum()
##########################################################################################
class Commodity_total(APIView):
    @extend_schema(
        description=readfile('Rest_API/endpoint_desc/commodity_total/desc.txt'),
        parameters=[
            OpenApiParameter(
                name='timeframe',
                description=readfile('Rest_API/endpoint_desc/commodity_total/timeframe.txt'),
            ),
            OpenApiParameter(
                name='option',
                description=readfile('Rest_API/endpoint_desc/commodity_total/option.txt'),
            ),
 
        ],
        examples=[
            OpenApiExample(
                'Example Year',
                value=e.commtotalExample1,
                media_type="application/json",
            ), 
            OpenApiExample(
                'Example TimeFrame',
                value=e.commtotalExample2,
                media_type="application/json",
            ),
           OpenApiExample(
                'Return Example',
                value=e.commtotalReturnExample,
                media_type="application/json",
            ),

        ],
        request=s.CommodityTotalSerializer(),
        responses={
            '200':s.CommodityTotalReturnSerializer(many=True)
        }
    )
    def post(self, request):
        serializer = s.CommodityTotalSerializer(data=request.data)
        if serializer.is_valid():
            #Send data to class and return data as pandas framework
            gen_query = CommodityTotal(
                serializer.validated_data['timeframe'],
                serializer.validated_data['option']
            )
 
            #Add ton value based on column and commodity type
            query  = gen_query.setup()
            if 'error' in query: return  Response(query) #error occured
            logger.info(f"CommodityTotal:{query}")
            lookup = QueryTool()
            self.df = lookup.query(query)                #data aquired
            
            commodities = lookup.query("SELECT description FROM c")["description"]
            #creating new dataframe that sorts data into sumations
            output = {
                "origin"   : [],
                "commodity": [],
                "option"   : [],
            }
            #exports
            ex = self.df.groupby(["Domestic_Origin", "Commodity"]).sum().reset_index() 
            ex = ex.drop(columns=['Domestic_Destination'])
            ex["Trade"] = "export"
            ex = ex.rename(columns={'Domestic_Origin': 'Place'})
            #imports
            im = self.df.groupby(["Domestic_Destination", "Commodity"]).sum().reset_index() 
            im = im.drop(columns=['Domestic_Origin'])
            im["Trade"] = "import"
            im = im.rename(columns={'Domestic_Destination': 'Place'})
            complete_df = pd.concat([ex, im])
            #create a response
            try:
                csv_data = complete_df.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = 'attachment; filename=TotalCommodity.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)
###########################################################################################
"""class ExportEndpoint(APIView):
    @extend_schema(
        description=readfile('Rest_API/endpoint_desc/exports/desc.txt'),
        parameters=[
            OpenApiParameter(
                name='origin',
                description=readfile('Rest_API/endpoint_desc/exports/origin.txt'),
            ),
            OpenApiParameter(
                name='timeframe',
                description=readfile('Rest_API/endpoint_desc/exports/timeframe.txt'),
            ),
 
        ],
        examples=[
            OpenApiExample(
                'Single Year Example',
                value=e.exportSingleExample1,
                media_type="application/json",
            ), 
            OpenApiExample(
                'Year Window Example',
                value=e.exportMultiExample2,
                media_type="application/json",
            ),
           OpenApiExample(
                'Return Example',
                value=e.exportReturnExample,
                media_type="application/json",
            )

        ],
        request=s.ExportsSerializer(),
        responses={
            '200':s.ExportsReturnSerializer(many=True)
        },
    )

    def post(self, request):
        serializer = s.ExportsSerializer(data=request.data)
        if serializer.is_valid():
            data = Export(
                serializer.validated_data['origin'],
                serializer.validated_data['timeframe']
            )
            query = data.setup()
            print(f"\n\n{query}\n\n")
            #sending query to server
            if query == False: return Response("Error: Check Data", 400)
            logger.info(f"Export Endpoint:{query}")
            lookup = QueryTool()
            data = lookup.query(query)

            #sending data
            try:
                csv_data = data.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = f'attachment; filename=exports_{serializer.validated_data["origin"]}.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)
"""
