from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from products.models import Products
from .forms import AddToCartProductForm


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })
    return render(request, 'cart/cart_detail.html', {
                  'cart': cart,
                  })


def add_to_cat_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity)

    return redirect('cart_detail')


def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


