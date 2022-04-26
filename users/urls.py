from django.urls import path
from . import views



urlpatterns = [
    path('cooks', views.cooks, name='cooks'),
    path('cook/<str:pk>', views.single_cook, name='cook'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('account/', views.account, name='account'),
    path('inbox/', views.inbox, name='inbox'),
    path('add-skill/', views.add_skill, name='add-skill'),
  
    path('update/<str:pk>', views.update_skill, name='update'),
    path('delete/<str:pk>', views.delete_skill, name='delete'),
    # path('recipy/<str:pk>/', views.single_recipy, name='recipy'),
    # path('add-recipy/', views.add_recipy, name='add-recipy'),
]