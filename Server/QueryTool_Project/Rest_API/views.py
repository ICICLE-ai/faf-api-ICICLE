#Rest_API/views.py
from django.shortcuts import render

from rest_framework.response   import Response
from rest_framework.decorators import api_view
from rest_framework.views      import APIView

from src.Data_Lookup import QueryTool
import Rest_API.serializers as s
from drf_spectacular.utils import extend_schema

    
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
            lookup  = QueryTool()
            details = lookup.colname(table)
            ser     = s.ListSerializer(data={'data': details})
            if ser.is_valid(): return Response(ser.data)
            Response(serializer.errors, status=400)
        Response(serializer.errors, status=400)
       

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
