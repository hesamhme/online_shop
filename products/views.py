from django.views import generic
from .models import Products

class ProductsListView(generic.ListView):
    model = Products
    template_name = 'products/procust_list_view.html'
