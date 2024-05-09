#Rest_API/serializers.py
from rest_framework import serializers

class QuerySerializer(serializers.Serializer):
    query = serializers.CharField(max_length=100000)

class EmptyPayLoadSerializer(serializers.Serializer):
    detail = serializers.CharField()

class ListSerializer(serializers.Serializer):
    data = serializers.ListField()
