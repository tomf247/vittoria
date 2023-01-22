
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,TemplateView
from django.contrib.sitemaps.views import sitemap
from home.sitemap import ProductSitemap,CategoriesSitemap
app_name = 'home'
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/', LogoutView.as_view(template_name='home/home.html'),name='logout'),
    path('edit-product/<product_id>', views.edit_product,name='edit-product'),
    path('delete-product/<product_id>', views.delete_product,name='delete-product'), 
    path('add-product/', views.add_product,name='add-product'), 
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),), 
    path('sitemap.xml', sitemap, {'sitemaps': {'products' : ProductSitemap,'categories':CategoriesSitemap}},
     name='django.contrib.sitemaps.views.sitemap') 
]