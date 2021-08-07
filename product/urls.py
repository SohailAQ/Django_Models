from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView
)

urlpatterns = [
    path('', ProductListView.as_view(), name="product-list"),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]