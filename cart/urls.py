from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('checkout/', views.checkout, name='checkout'),
]
