from rest_framework import serializers
from .models import User, Watchlist

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.save()
        return user

class WatchlistSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    stocks = serializers.ListField(child=serializers.CharField(max_length=10))

    def create(self, validated_data):
        watchlist = Watchlist(
            user_id=validated_data['user_id'],
            stocks=validated_data['stocks']
        )
        watchlist.save()
        return watchlist
