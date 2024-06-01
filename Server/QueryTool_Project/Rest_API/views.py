#Rest_API/views.py
from django.shortcuts import render
from django.http      import HttpResponse
import pandas as pd
from io import StringIO


from rest_framework.response   import Response
from rest_framework.decorators import api_view
from rest_framework.views      import APIView

from src.Data_Lookup import QueryTool
from src.GrabTable import GrabTable
from src.PointToPoint import PointToPoint
import Rest_API.examples as e
import Rest_API.serializers as s


from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse
import logging
    
logger = logging.getLogger('Rest_API.views')

###########################################################################################
class GatherAll(APIView):
    @extend_schema(
        description="This endpoint queries the FAF database and retrieves one of six fully populated tables: faf0, faf1, faf2, faf3, state0, state1, state2, or state3. Subsequently, the server generates a query to join these smaller tables with the main data tables and processes this query. The resulting data is stored in a Pandas DataFrame, converted to a CSV file, and provided to the user as a downloadable file. The file is named according to the selected table. If the user inputs incorrect information, an error message is returned detailing the issue.",
        examples=[
            OpenApiExample(
                'Example',
                value = e.tableModel_example,
                media_type="application/json",
            )
        ],
        request=s.TableSerializer(),
        responses={
            '200': OpenApiResponse(
                description= "CSV download of joined data table",
                examples=[
                    OpenApiExample(
                        'CSV Example',
                        value=e.table_CSVExample,
                        media_type='text/csv'
                    )
                ],
            )
        }
    )
    def post(self, request):
        serializer = s.TableSerializer(data=request.data)
        if serializer.is_valid():
            table  = serializer.validated_data['table']
            gt   = GrabTable(table)
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
                return Reponse("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)

###########################################################################################
class PointtoPoint(APIView):
    @extend_schema(
        description="Takes a specific commodity, or all of them, and shows the amount traded between two states in a specific year or time frame",
        examples=[
            OpenApiExample(
                'Single Year Example',
                value=e.PointToPointExample1,
                media_type="application/json",
            ),
            OpenApiExample(
                'Year Range Example',
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
        #response=s.PtoPReturnSerializer
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
            logger.info(f"PointToPoint: {query}")
            return Response(query)
        return Response(serializer.errors, status=400)

    def merp(self, request):
        serializer = s.TableSerializer(data=request.data)
        if serializer.is_valid():
            table  = serializer.validated_data['table']
            gt   = GrabTable(table)
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
                return Reponse("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)


##########################################################################################
class Exports(APIView):
    @extend_schema(
        description="Shows all of the exports from a region/state based on year or time frame. The destination, transport type and the time also are supplied",
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
        }
    )

    def post(self, request):
        return Response("Exports is up!")
##########################################################################################
class Imports(APIView):
    @extend_schema(
        description="Shows all of the imports from a region/state based on year or time frame. The origin, transport type, commodity, ton amount, and year are also supplied.",
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
        return Response("Import is up!")
##########################################################################################
class RawResource(APIView):
    @extend_schema(
        description="Adds up total tons per commodity based on year or year frame and orders based on ton. It has options for imports and/or exports",
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
        return Response("Raw is up!")
##########################################################################################
class Commodity_total(APIView):
    @extend_schema(
        description="Takes the commodities in each state and adds up their total based on import, export or both and sorts the return based on ton amount. The time frame is based on year or year frame, and the return will give the location of the ranked commodity and if it was imported or exported",
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
        return Response("Commodity total is up!")
##########################################################################################
class Ratio_ie(APIView):
    @extend_schema(
        description="gives a ratio of commodities imported/exported in stated ordered by resource",
        examples=[
            OpenApiExample(
                'Ratio Example Year',
                value=e.ratioExample1,
                media_type="application/json",
            ), 
            OpenApiExample(
                'Ratio Example TimeFrame',
                value=e.ratioExample2,
                media_type="application/json",
            ),
           OpenApiExample(
                'Ratio Return Example',
                value=e.ratioReturnExample,
                media_type="application/json",
            ),

        ],
        request=s.RatioSerializer(),
        responses={
            '200':s.RatioReturnSerializer()
        }
    )
   
    def post(self, request):
        return Response("Ratio is ratioing!")
##########################################################################################
class TablePayLoad(APIView):
    @extend_schema(
        description="Returning a list of the table names from database",
        request=None,
        responses=s.ListSerializer
    )
    def get(self, request):
        query  = QueryTool()
        tables = query.show_tables()
        ser    = s.ListSerializer(data={'data':tables})
        if ser.is_valid(): return Response(ser.data)
        return Response(serializer.errors, status=400)

class QueryLoader(APIView):
    @extend_schema(
        request    =s.QuerySerializer,
        description="Take a query and return output from mySQL server",
        responses  =s.ListSerializer
    )
    def post(self, request):
        serializer = s.QuerySerializer(data=request.data)
        if serializer.is_valid():
            cmd    = serializer.validated_data['query']
            logger.info(f"query: {cmd}")                            #logging the commands used
            lookup = QueryTool()
            data   = lookup.query(cmd)
            ser    = s.ListSerializer(data={'data': data})
            if ser.is_valid(): return Response(ser.data)
            return Response(serializer.errors, status=400)
        return Response(serializer.errors, status=400)

class TableDescripter(APIView):
    @extend_schema(
        request    =s.QuerySerializer,
        description="takes in a table name and returns the column data",
        responses  =s.ListSerializer
    )
    def post(self, request):
        serializer = s.QuerySerializer(data=request.data)
        if serializer.is_valid():
            table   = serializer.validated_data['query']
            logger.info(f"col: {table}")
            lookup  = QueryTool()
            details = lookup.colname(table)
            ser     = s.ListSerializer(data={'data': details})
            if ser.is_valid(): return Response(ser.data)
            return Response(serializer.errors, status=400)
        return Response(serializer.errors, status=400)
       
####################################User End#########################################
class GetTable(APIView):
    @extend_schema(
        request    = s.DataQuerySerializer,
        description="Takes multiple attributes and returns data that fits",
        responses  = s.ListSerializer
    )

    def post(self, request):
        serializer = s.DataQuerySerializer(data=request.data)
        if serializer.is_valid():
            query = CreateQuery(
                serializer.validated_data['table'],
                serializer.validated_data['origin'],
                serializer.validated_data['destination'],
                serializer.validated_data['commodity'],
                serializer.validated_data['transport'],
                serializer.validated_data['distance'],
                serializer.validated_data['ton_year'],
                serializer.validated_data['val_year'],
                serializer.validated_data['currVal_year'],
                serializer.validated_data['tmile'],
                serializer.validated_data['tonHigh_year'],
                serializer.validated_data['tonLow_year'],
                serializer.validated_data['valHigh_year'],
                serializer.validated_data['valLow_year'],
                serializer.validated_data['limit']
            )
            if query.help(): return Response(query.help())
            query = query.setup()
            logger.info(f"Query Build: {query}")

            lookup = QueryTool()
            data = lookup.query(query)

            ser = s.ListSerializer(data={'data':data})
            if ser.is_valid(): return Response(ser.data)
            return Response(serializer.errors, status=400)
        return Response(serializer.errors, status=400)

