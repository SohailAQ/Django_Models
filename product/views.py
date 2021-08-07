from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView
)
from django.views.generic.edit import UpdateView
from .models import Product


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'ingredients', 'price', 'quantity']


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView, UserPassesTestMixin):
    model = Product
    fields = ['name', 'ingredients', 'price', 'quantity']

    def test_func(self):
        username = self.request.user.username
        print(username)
        if username == 'buyer':
            return True
        else:
            raise Http404("You are not allowed to update")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/product'