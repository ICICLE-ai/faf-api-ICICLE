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
    timeframe  = serializers.ListField(max_length=2, child=serializers.IntegerField())

class ExportsReturnSerializer(serializers.Serializer):
    destination = serializers.CharField(max_length=15)
    commodity   = serializers.CharField(max_length=10)
    ton         = serializers.FloatField()
    transport   = serializers.CharField(max_length=10)
    year        = serializers.IntegerField()


class ImportsSerializer(serializers.Serializer):
    area      = serializers.CharField(max_length=15)
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

