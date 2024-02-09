from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Categories, Orders


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'title']


class OrderSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='ower.username')

    class Meta:
        model = Orders
        fields = ['id', 'date_of_order', 'categories', 'nickname',
                  'age', 'description', 'owner']


class UserSerializers(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']
