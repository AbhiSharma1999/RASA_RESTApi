from rest_framework import serializers

class RequestSerializer(serializers.Serializer):
    sender = serializers.CharField()
    message = serializers.CharField()

class RespSerializer(serializers.Serializer):
    recipient_id = serializers.CharField()
    text = serializers.CharField()