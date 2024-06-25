from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, MenuItem, Cart, Order, OrderItem

# Serializers define the API representation.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'description', 'ingredients', 'featured', 'category', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 2}
        }
        depth = 1
        

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'menuitem', 'quantity', 'unit_price', 'price']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'delivery_crew', 'status', 'total', 'date']