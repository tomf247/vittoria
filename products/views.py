from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

# Adding Filters and Search for shop.html
def shop(request):
    category = 'All'
    gender = 'All'
    sort_by = None
    query = request.GET.get('query')
    category = request.GET.get('category')
    sort_by = request.GET.get('sort_by')
    gender = request.GET.get('gender')
    products = Product.objects.all()
    categories = Category.objects.all()
    p = Paginator(products,15)   
    page = request.GET.get('page')
    paged_products = p.get_page(page)
    nums = "a" * paged_products.paginator.num_pages
    products = p.get_page(page)
    
    
    if query: # Looking for the entered query if a product matches any of these fileds  # here category is a foreign key
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)| Q(category__name__icontains=query))
        p = Paginator(products,15)   
        
        page = request.GET.get('page')
        paged_products = p.get_page(page)
        nums = "a" * paged_products.paginator.num_pages
        products = p.get_page(page)
    if category:
        products = Product.objects.filter(category__name = category)
                  # Pagination
       
    if gender:
        products = Product.objects.filter(gender = gender)
    if sort_by == 'name-ascending':
        products = Product.objects.all().order_by('name')
    if sort_by == 'name-descending':
        products = Product.objects.all().order_by('-name')
    if sort_by == 'price-low-to-high':
        products = Product.objects.all().order_by('price')
    if sort_by == 'price-high-to-low':
        products = Product.objects.all().order_by('-price')
        
    
    # Pagination -  here 15 is the total products to be shown per page
   
    context = {
        'products':products,
        'query':query,
        'nums':nums,
        'categories':categories,
        'category':category,
        'gender':gender,
        'sort_by':sort_by
    }
    return render(request,'products/shop.html',context)

def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    featured_products = Product.objects.filter(category=product.category)
    return render(request,'products/product-details.html',{'product':product,'featured_products':featured_products})