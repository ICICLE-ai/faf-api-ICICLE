#Rest_API/serializers.py
from rest_framework import serializers

class QuerySerializer(serializers.Serializer):
    query = serializers.CharField(max_length=1000000)

class EmptyPayLoadSerializer(serializers.Serializer):
    detail = serializers.CharField()

class ListSerializer(serializers.Serializer):
    data = serializers.ListField()

class DataQuerySerializer(serializers.Serializer):
    table        = serializers.CharField(max_length=20)
    origin       = serializers.BooleanField()
    destination  = serializers.BooleanField()
    commodity    = serializers.BooleanField()
    transport    = serializers.BooleanField()
    distance     = serializers.BooleanField()
    ton_year     = serializers.ListField(child=serializers.CharField())
    val_year     = serializers.ListField(child=serializers.CharField())
    currVal_year = serializers.ListField(child=serializers.CharField())
    tmile        = serializers.ListField(child=serializers.CharField())
    tonHigh_year = serializers.ListField(child=serializers.CharField())
    tonLow_year  = serializers.ListField(child=serializers.CharField())
    valHigh_year = serializers.ListField(child=serializers.CharField())
    valLow_year  = serializers.ListField(child=serializers.CharField())
    limit        = serializers.IntegerField()

