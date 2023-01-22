from django.urls import path
from .import views
app_name ="cart"
urlpatterns = [
    path("cart/",views.cart,name='cart'),
    path("add-to-cart/<product_id>/",views.add_to_cart,name="add-to-cart"),
    path("update-cart/<product_id>/",views.update_cart,name="update-cart"),
    path("remove-from-cart/<product_id>/",views.remove_from_cart,name="remove-from-cart"),
    path("wishlist/",views.wishlist,name="wishlist"),
    path("add-to-wishlist/<product_id>",views.add_to_wishlist,name="add-to-wishlist"),
    path("remove-from-wishlist/<product_id>",views.remove_from_wishlist,name="remove-from-wishlist")


]