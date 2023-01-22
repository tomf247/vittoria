from django.shortcuts import render,redirect,get_object_or_404
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def cart(request):
    cart = request.session.get('cart',{})
    print(cart)
    return render(request,"cart/cart.html")

def add_to_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity', 1)) 
    cart = request.session.get('cart',{})

    if product_id in list(cart.keys()):
        print("quantity update")
        cart[product_id]['quantity'] = cart[product_id]['quantity'] + quantity
        messages.success(request,"Your cart was updated")
    else:
        #cart[product_id] = product_id
        cart[product_id]    = {'quantity': quantity, 'price': float(product.price)}
        messages.success(request,'Item was added to cart')
    request.session['cart']= cart
    return redirect("/cart")

def remove_from_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart',{})
    cart.pop(product_id)
    request.session['cart'] = cart

    messages.success(request,"Item has been removed from your cart.")
    return redirect("/cart")

def update_cart(request,product_id):
    cart = request.session.get('cart',{})
    print(product_id)
    quantity = int(request.POST.get('quantity'))
    if product_id in list(cart.keys()):
        print("quantity update")
        cart[product_id]['quantity'] = quantity
        print(cart)
        messages.success(request,"Your cart was updated")
    else:
        messages.info(request,'There was some issue with updating your cart')
        return redirect("/cart")
    request.session['cart']= cart
    return redirect("/cart")

@login_required(login_url='home:login')
def add_to_wishlist(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = Wishlist.objects.all()

    if wishlist_item.filter(product__id=product.id).exists():
            messages.info(request, "This item is already on your Wishlist.")
            return redirect("cart:wishlist")
    else:
        wishlist_item = Wishlist.objects.create(
        user=request.user, product=product)
        messages.info(request, "Item added to your wishlist.")
        return redirect("cart:wishlist")

@login_required(login_url='home:login')
def remove_from_wishlist(request,product_id):
    wishlist = Wishlist.objects.filter(user=request.user,product__id=product_id)
    wishlist.delete()
    messages.info(request,"Item removed from your wishlist !")
    return redirect('cart:wishlist')

@login_required(login_url='home:login')
def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request,"cart/wishlist.html",{'wishlist':wishlist})