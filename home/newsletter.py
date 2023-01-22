from django.shortcuts import render
from .models import Newsletter
from .forms import NewsletterForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def newsletter(request):
    newsform = NewsletterForm()
    news = Newsletter.objects.all()
    if request.method=='POST':
        print('post')
        if request.POST.get("form_type") == 'newsletter':
            newsform=NewsletterForm(request.POST)
            if newsform.is_valid():
                print('valid')
                email = request.POST.get('email')
                send_mail(
                subject=f'Newsletter Vittoria Ecommerce',
                message=f'Hi {email}  Thanks for subscribing to our Newsletter, \n The Vittoria Ecommerce Team',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]) #this email account receives the damage claim notification
                newsform.save()
                messages.info(request,'Thank you for subscribing to our Newsletter')
    return{'newsform':newsform}