from django.urls import path, include
from . import views



urlpatterns = [
    path('products/',views.ProductView.as_view() ),
    path('products/<int:pk>/', views.SingleProductView.as_view()), 
    path('brands/', views.BrandView.as_view()), 
]