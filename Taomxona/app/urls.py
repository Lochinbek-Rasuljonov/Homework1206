from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('foods/', views.all_foods, name='all_foods'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
    path('category/<int:category_id>/', views.category_foods, name='category_foods'),
    path('food/add/', views.add_food, name='add_food'),
    path('food/edit/<int:food_id>/', views.edit_food, name='edit_food'),
]