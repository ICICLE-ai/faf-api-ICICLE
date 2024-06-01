#Rest_API/serializers.py
from rest_framework import serializers

class TableSerializer(serializers.Serializer):
    table = serializers.CharField(max_length=6)

class PointToPointSerializer(serializers.Serializer):
    commodity   = serializers.CharField(max_length=40)
    origin      = serializers.CharField(max_length=40)
    destination = serializers.CharField(max_length=40)
    timeframe   = serializers.ListField(max_length=2, child=serializers.IntegerField())

class PtoPReturnSerializer(serializers.Serializer): 
    commodity = serializers.CharField(max_length=10)
    ton       = serializers.FloatField()
    transport = serializers.CharField(max_length=10)
    year      = serializers.IntegerField()


class ExportsSerializer(serializers.Serializer):
    origin     = serializers.CharField(max_length=15)
    timeframe = serializers.ListField(max_length=2, child=serializers.IntegerField())

class ExportsReturnSerializer(serializers.Serializer):
    destination = serializers.CharField(max_length=15)
    commodity   = serializers.CharField(max_length=10)
    ton         = serializers.FloatField()
    transport   = serializers.CharField(max_length=10)
    year        = serializers.IntegerField()


class ImportsSerializer(serializers.Serializer):
    origin    = serializers.CharField(max_length=15)
    timeframe = serializers.ListField(max_length=2, child=serializers.IntegerField())

class ImportsReturnSerializer(serializers.Serializer):
    destination = serializers.CharField(max_length=15)
    commodity   = serializers.CharField(max_length=10)
    ton         = serializers.FloatField()
    transport   = serializers.CharField(max_length=10)
    year        = serializers.IntegerField()


class RawResourceSerializer(serializers.Serializer):
    origin    = serializers.CharField(max_length=15)
    timeframe = serializers.ListField(max_length=2, child=serializers.IntegerField())
    option    = serializers.CharField(max_length=6)
    
class RawResourceReturnSerializer(serializers.Serializer):
    commodity = serializers.CharField(max_length=10)
    ton       = serializers.FloatField()
    option    = serializers.CharField(max_length=6)


class CommodityTotalSerializer(serializers.Serializer):     
    commodity = serializers.CharField(max_length=10)
    timeframe = serializers.ListField(max_length=2, child=serializers.IntegerField())
    option    = serializers.CharField(max_length=6)

class CommodityTotalReturnSerializer(serializers.Serializer):
    origin    = serializers.CharField(max_length=15)
    ton       = serializers.FloatField()
    option    = serializers.CharField(max_length=6)


class RatioSerializer(serializers.Serializer):
    origin    = serializers.CharField(max_length=15)
    timeframe = serializers.ListField(max_length=2, child=serializers.IntegerField())

class RatioReturnSerializer(serializers.Serializer):
    commodity  = serializers.CharField(max_length=10)
    ratio      = serializers.FloatField()
    ton_import = serializers.FloatField()    
    ton_export = serializers.FloatField()

##################

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

