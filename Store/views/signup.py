from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from ..models.customer import Customer
from django.views import View


class Signup(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('password')
        # validation
        value = {
            'name': name,
            'email': email,
            'phone': phone,
            'password': password
        }
        customer = Customer(name=name,
                            email=email,
                            phone=phone,
                            password=password
                            )
        error_msg = self.validateCustomer(customer)

        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("home")
        else:
            data = {
                'error': error_msg,
                'values': value,
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_msg = None
        if len(customer.name) < 4:
            error_msg = 'name must be more than four char'
        elif not customer.name:
            error_msg = 'full name required'
        elif len(customer.phone) < 9:
            error_msg = 'you forget the phone number  please check '
        elif not customer.phone:
            error_msg = 'phone number required'
        elif len(customer.email) < 9:
            error_msg = 'please check email more than 9 char'
        elif not customer.email:
            error_msg = 'email required'
        elif len(customer.password) < 7:
            error_msg = ' please enter password more than 7 character'
        elif not customer.password:
            error_msg = 'password required'
        elif customer.email_exist():
            error_msg = "Email ID already registered"
        return error_msg
