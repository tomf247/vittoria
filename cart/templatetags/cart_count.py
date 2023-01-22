from django import template
register = template.Library()

@register.filter(name='total_items')
def total_items(quantity):
    return quantity

@register.filter(name='cart_total')
def cart_total(quantity,price):
    return price*quantity
