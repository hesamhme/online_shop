from products.models import Products


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            self.session['cart'] = {}
            cart = self.session['cart']

        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)

        if not quantity:
            self.cart.pop(product_id, False)  # remove from the cart
        else:
            item = self.cart.setdefault(product_id, {})
            item['quantity'] = quantity  # set quantity, not add
        self.save()

        # if product_id not in self.cart:
        #     self.cart[product_id] = {'quantity': 0}
        # else:
        #     self.cart[product_id]['quantity'] += quantity
        # self.save()

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        products_id = self.cart.keys()
        products = Products.objects.filter(id__in=products_id)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product
        for item in cart.values():
            yield item

    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        products_id = self.cart.keys()
        products = Products.objects.filter(id__in=products_id)
        return sum(product.price for product in products)
