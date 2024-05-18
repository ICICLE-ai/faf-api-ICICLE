#Rest_API/views.py
from django.shortcuts import render

from rest_framework.response   import Response
from rest_framework.decorators import api_view
from rest_framework.views      import APIView

from src.Data_Lookup import QueryTool
from src.CreateQuery import CreateQuery
import Rest_API.serializers as s
from drf_spectacular.utils import extend_schema
import logging
    
logger = logging.getLogger('Rest_API.views')

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



class GetTableA(APIView):
    @extend_schema(
        request    = s.QuerySerializer,
        description="Takes in one of the faf or state tables and gives full data back",
        responses  =s.ListSerializer
    )
    def get(self, request, table_id):
        tab_dict = {
            "_faf551_faf_0": "faf0",
            "_faf551_faf_1": "faf1",
            "_faf551_faf_2": "faf2",
            "_faf551_faf_3": "faf3",
            "_faf551_state_0": "state0",
            "_faf551_state_1": "state1",
            "_faf551_state_2": "state2",
            "_faf551_state_3": "state3"
        }
        query = ""
        try:
            with open(f'src/queries/{tab_dict[table_id]}.sql', 'r') as fp:
                query = "".join(sentence for sentence in fp)
            lookup = QueryTool()
            data   = lookup.query(query)
            ser    = s.ListSerializer(data={'data': data})
            if ser.is_valid(): return Response(ser.data)
            return Response(serializer.errors, status=400)
        except:
            return Response(status=400)


"""
@api_view(['GET'])
def getHelp(request):
    query = QueryTool()
    cmds  = query.list_commands()
    return Response(cmds)

@api_view(['GET'])
def getCommodities(request):
    print("\n\nsomething\n\n")
    query      = QueryTool()
    resources  = query.allResources()
    return Response(resources) 

@api_view(['GET', 'POST'])
def getQuery(request):
    serializer = QuerySerializer(data=request.data)
    if serializer.is_valid():
        query = serializer.validated_data['query']
        
        lookup = QueryTool()
        data = lookup.query(query)
        return Response(data)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def getColumnName(request):
    serializer = QuerySerializer(data=request.data)
    if serializer.is_valid():
        table = serializer.validated_data['query']
        lookup = QueryTool()
        return Response(lookup.colname(table))
    else:
        return Response(serializer.errors, status=400)
"""
