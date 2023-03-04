from django.urls import path
from .views import cart_detail_view, add_to_cat_view, remove_cart
urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/', add_to_cat_view, name='cart_add'),
    path('remove/<int:product_id>/', remove_cart, name='cart_remove'),
]
