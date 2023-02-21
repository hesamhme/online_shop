from django.urls import path
from .views import ProductsListView, ProductDetails, CommentCreatView

urlpatterns = [
    path('', ProductsListView.as_view(), name='list_view'),
    path('<int:pk>/', ProductDetails.as_view(), name='detail_view'),
    path('comment/<int:product_id>/', CommentCreatView.as_view(), name='comment_crate'),



]
