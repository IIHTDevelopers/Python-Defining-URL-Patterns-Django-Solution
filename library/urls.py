# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
]
