"""
URL configuration for the inventory_receiving app.
"""
from django.urls import path
from . import views

app_name = 'inventory_receiving'

urlpatterns = [
    # Dashboard
    path('', views.DashboardView.as_view(), name='dashboard'),
    
    # Product Type URLs
    path('product-types/', views.ProductTypeListView.as_view(), name='product_type_list'),
    path('product-types/create/', views.ProductTypeCreateView.as_view(), name='product_type_create'),
    path('product-types/<int:pk>/', views.ProductTypeDetailView.as_view(), name='product_type_detail'),
    path('product-types/<int:pk>/edit/', views.ProductTypeUpdateView.as_view(), name='product_type_edit'),
    
    # Product URLs
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<slug:sku>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<slug:sku>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('products/<slug:sku>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    
    # Product Image URLs
    path('products/<slug:sku>/images/add/', views.ProductImageCreateView.as_view(), name='product_image_create'),
    path('images/<int:pk>/delete/', views.ProductImageDeleteView.as_view(), name='product_image_delete'),
]
