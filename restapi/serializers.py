from rest_framework import serializers


class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()
