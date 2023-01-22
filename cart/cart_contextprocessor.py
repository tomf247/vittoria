from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404
from cart.models import Wishlist

def cart_products(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    unique_product_count = 0
    unique_product_ids = set()

    for product_id, product_data in cart.items():
            product = get_object_or_404(Product, id=product_id)
            unique_product_ids.add(product_id)
            total = total+product_data['quantity'] * product.price
            product_count += product_data['quantity']
            product = Product.objects.get(id=product_id)
            cart_items.append({
                'product':product,
                'quantity':product_data['quantity']
            })
    unique_product_count = len(unique_product_ids)
        
   
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'cart_count':unique_product_count,
        'cart':cart,
       
    }

    return context

def wishlist_count(request):
    wishlist_total = 0

    if request.user.is_authenticated:
        wishlist_total = Wishlist.objects.filter(user=request.user).count()
    else:
        wishlist_total = 0
    context = {
        'wishlist_total':wishlist_total
    }
    return context
