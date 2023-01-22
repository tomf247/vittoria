import os
from django.shortcuts import render,redirect
from django.conf import settings
from .forms import CheckoutForm
from .models import Order, OrderedItem
from products.models import Product
from cart.cart_contextprocessor import cart_products
import stripe
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def checkout(request):
    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.environ.get('STRIPE_SECRET_KEY')
    if request.method =='POST':
        cart = request.session.get('cart',{})
        form = CheckoutForm(request.POST)
        if form.is_valid():
            stripe_token = request.POST.get("stripe_token")
            pid = request.POST.get('client_secret').split('_secret')[0]
            order = Order()
            order.name = form.cleaned_data['name']
            order.email = form.cleaned_data['email']
            order.country = form.cleaned_data['country']
            order.phone = form.cleaned_data['phone']
            order.street_name = form.cleaned_data['street_name']
            order.apartment_name = form.cleaned_data['apartment_name']
            order.postal_code = form.cleaned_data['postal_code']
            order.city_name = form.cleaned_data['city_name']
            order.name = form.cleaned_data['name']
            order.stripe_pid = pid
            if request.user.is_authenticated:
                order.user = request.user
            else:
                order.user = None
            order.save()
            total = 0
            print(cart)
            for product_id,product_data in cart.items():
                product = Product.objects.get(id=product_id)
                ordered_item = OrderedItem(
                    order=order,product=product,quantity=product_data['quantity']
                )
                ordered_item.save()
                total +=product_data['quantity']*product.price
            order.total = total
            order.save()
            charge = stripe.Charge.create(
                    amount=int(total * 100), # Amount in Cents
                    currency='USD',
                    description='Charge From Vittoria Ecommerce',
                    source=stripe_token
                )
            return redirect("order:success",order.id)
        else:
            messages.warning(request,form.errors)
            messages.warning(request,"Please check your form")

            return redirect("/checkout")
        
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Sorry, your cart is empty")
            return redirect('cart:cart')
        cart_recent = cart_products(request)
        total = cart_recent['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='usd',
        )
        form = CheckoutForm()

    
    context = {
        'form':form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'order/checkout.html', context)


def checkout_success(request,OrderID):
    messages.success(request,"Thank you for shopping with us")
    order = Order.objects.get(id=OrderID)
    ordered_item = OrderedItem.objects.filter(order__id=OrderID)
    send_mail(
    subject=f'Item Purchase Vittoria Ecommerce',
    message=f'Hi {order.email} We are busy preparing your order. \n Thanks for Shopping with us,\n The Vittoria Ecommerce Team',
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=[order.email])
    if 'cart' in request.session:
        del request.session['cart']
    return render(request,"order/success.html",{'order':order,'ordered_item':ordered_item})