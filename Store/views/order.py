from django.shortcuts import render, redirect
from django.views import View
from Store.models import Order


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_order_cust_id(customer)
        print("order", orders)
        return render(request, 'order.html', {'orders': orders})
