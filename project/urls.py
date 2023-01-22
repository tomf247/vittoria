
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.conf.urls import handler404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('products.urls')),
    path('',include('cart.urls')),
    path('',include('order.urls')),
    path('forgotpassword/', PasswordResetView.as_view(template_name='account/forgotpassword.html'),name='forgotpassword'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='account/forgot_password_emailed.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='account/new_password.html'),name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),

]
handler404 = 'home.views.error_404'
