from django.shortcuts import render
from products.models import * # Importing all models with *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages #import messages
from .forms import SignupForm, EditProductForm
from django.contrib.auth.decorators import user_passes_test
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context ={
        'products':products,
        'categories':categories,
    }
    return render(request,'home/home.html',context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print('signup post')
        if form.is_valid():
            print('valid')
            form.save()
            messages.success(request,'Signup Successful')
            return redirect('home:login')
        else:
            messages.error(request, form.errors)
        
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Log In Success")
            return redirect('/')
        else:
            messages.warning(request,"Invalid Login details")
            return redirect('home:login')
    else:
        return render(request, 'account/login.html')

@user_passes_test(lambda u: u.is_superuser,login_url='adminlogin')
def edit_product(request,product_id):
    product = Product.objects.get(id=product_id)
    form = EditProductForm(instance=product)
    if request.method == "POST":
        form = EditProductForm(request.POST,instance=product)
        
        if form.is_valid():

            product.save()
            messages.success(request,"The product details have been updated successfully")
            return redirect("home:edit-product",product_id)
        else:
            messages.error(request,"Please fill the form appropriately",form.errors)
            return redirect("home:edit-product",product_id)
    
    context = {
        'product':product,
        'form':form
    }
    return render(request,'home/edit-product.html',context)

@user_passes_test(lambda u: u.is_superuser,login_url='adminlogin')
def delete_product(request,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.info(request,'The product has been deleted !')
    return redirect("/")

def error_404(request, exception):
    return render(request, '404.html')

@user_passes_test(lambda u: u.is_superuser,login_url='adminlogin')
def add_product(request):
    form= AddProductForm()
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"New Product has been added successfully")
            return redirect("products:shop")
        else:
            messages.error(request,"Please fill the form appropriately",form.errors)
            return redirect("home:add-product")
    
    context = {
        'form':form
    }
    return render(request,'home/add-product.html',context)
