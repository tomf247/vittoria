
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
   
    path('shop/',views.shop,name='shop'),
    path('product-detail/<product_id>/',views.product_detail,name='product-detail')
    
]