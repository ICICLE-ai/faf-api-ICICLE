from django.shortcuts import render

from rest_framework.response   import Response
from rest_framework.decorators import api_view

from src.Data_Lookup import QueryTool
from .serializers import QuerySerializer

@api_view(['GET'])
def getData(request):

    query  = QueryTool()
    tables = query.show_db()
    return Response(tables)

@api_view(['POST', 'GET'])
def getQuery(request):
    serializer = QuerySerializer(data=request.data)
    if serializer.is_valid():
        query = serializer.validated_data['query']
        print(query)
        lookup = QueryTool()
        data = lookup.query(query)
        return Response(data)
    else:
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def getColumnName(request):
    serializer = QuerySerializer(data=request.data)
    if serializer.is_valid():
        table = serializer.validated_data['query']
        lookup = QueryTool()
        return Response(lookup.colname(table))
    else:
        return Response(serializer.errors, status=400)
