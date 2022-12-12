from django.shortcuts import render, redirect
from Store.models.product import Product
from django.views import View


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_prod_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})