from django.urls import path
from .views import register_view, login_view, display_products_view, place_order_view, view_orders_view, pro

urlpatterns = [
    path('', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('products/<str:username>/', display_products_view, name='products'),
    path('place-order/<str:username>/', place_order_view, name='place_order'),
    path('view-orders/<str:username>/', view_orders_view, name='view_orders'),
    path("pro/", pro, name="products")
]
