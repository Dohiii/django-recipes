from django.urls import path
from . import views



urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('recipe/<str:pk>/', views.single_recipe, name='recipe'),
    path('add-recipe/', views.add_recipe, name='add-recipe'),
    path('update/<str:pk>', views.update_recipe, name='update-recipe'),
    path('delete/<str:pk>', views.delete_recipe, name='delete-recipe'),
]