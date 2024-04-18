from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from src.Data_Lookup import QueryTool

@api_view(['GET'])
def getData(request):

    query = QueryTool()
    query.connectSQL()
    test = query.tables()

    return Response(test)
