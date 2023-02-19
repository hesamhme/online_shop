from django.views import generic
from .models import Products


class ProductsListView(generic.ListView):
    # queryset = Products.objects.filter('active')
    model = Products
    template_name = 'products/procust_list_view.html'


class ProductDetails(generic.DetailView):
    model = Products
    template_name = 'products/products_detail_view.html'
    context_object_name = 'pro'
