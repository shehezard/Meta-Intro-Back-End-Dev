from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, MenuItem, Cart, Order, OrderItem

# Serializers define the API representation.
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category']