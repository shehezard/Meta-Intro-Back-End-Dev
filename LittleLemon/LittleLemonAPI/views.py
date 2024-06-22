from django.shortcuts import render
from rest_framework import generics
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import MenuItemSerializer
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the LittleLemonAPI index.")

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer