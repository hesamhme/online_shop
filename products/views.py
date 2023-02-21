from django.views import generic
from django.shortcuts import get_object_or_404


from .models import Products, Comment
from .forms import CommentForm


class ProductsListView(generic.ListView):
    # queryset = Products.objects.filter('active')
    model = Products
    template_name = 'products/products_list_view.html'


class ProductDetails(generic.DetailView):
    model = Products
    template_name = 'products/products_detail_view.html'
    context_object_name = 'pro'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreatView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Products, id=product_id)
        obj.product = product
        return super().form_valid(form)


