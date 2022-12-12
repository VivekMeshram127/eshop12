from django.shortcuts import render, redirect
from django.views import View
from Store.models import Product
from Store.models import Customer
from Store.models import Order


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        print(address, phone, customer)
        cart = request.session.get('cart')
        products = Product.get_prod_by_id(list(cart.keys()))
        print("check prod", products)

        for prod in products:
            print("error", cart.get(prod.id))
            order = Order(customer=Customer(id=customer),
                          product=prod,
                          price=prod.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(prod.id))
                          )
            order.save()
        request.session['cart'] = {}
        return redirect('cart')
