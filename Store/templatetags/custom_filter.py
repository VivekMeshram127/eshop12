from django import template

register = template.Library()


@register.filter(name='currency')
def currency(number):
    return "₹ " + str(number)


@register.filter(name='multiply')
def multiply(num, num1):
    return num * num1
