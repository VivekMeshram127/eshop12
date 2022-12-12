from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models.product import Product
from ..models.category import Category
from django.views import View


# Create your views here.

class Index(View):


    def post(self, request):
        product = request.POST.get('prod')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart = {product: 1}
        request.session['cart'] = cart
        print("cart add check", request.session['cart'])
        return redirect('home')


    def get(self, request):

        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        product = None
        # request.session.clear()
        category = Category.get_all_category()
        categoryId = request.GET.get('category')
        if categoryId:
            print('check home',product)
            product = Product.get_prod_id(categoryId)
        else:
            product = Product.get_all_product()
        data = {'product': product, 'category': category}
        print("your email id is 1", request.session.get('email'))
        return render(request, 'index.html', data)
        # return HttpResponse("hellow")
