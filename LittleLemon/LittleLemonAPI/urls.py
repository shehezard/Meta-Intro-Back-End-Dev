from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('categories/<int:pk>/', views.SingleCategoryView.as_view()),
    path('users/', views.UserView.as_view()),
    path('users/<int:pk>/', views.SingleUserView.as_view()),
]