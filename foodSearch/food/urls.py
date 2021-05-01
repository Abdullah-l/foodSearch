from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'), 
    #path('voicenote/success', views.vn_success, name='vn_success'),
    path('foodS/', views.foodS, name='foodS'),
    path('restaurantS/', views.restaurantS, name='restaurantS'),
    path('cuisineS/', views.cuisineS, name='cuisineS'),
    path('restaurant/<int:id>', views.restaurant, name='restaurant'),
]