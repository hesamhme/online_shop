from django.urls import path
from .views import ProductsListView, ProductDetails

urlpatterns = [
    path('', ProductsListView.as_view(), name='list_view'),
    path('<int:pk>/', ProductDetails.as_view(), name='detail_view'),



]
