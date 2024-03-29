from .models import Newsletter
from .forms import NewsletterForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from email_validator import validate_email, EmailNotValidError

def newsletter(request):
    news = Newsletter()
    if request.method=='POST':
        if request.POST.get("form_type") == 'newsletter':
                email = request.POST.get('email')
                try:
                    is_new_account = True
                    validation = validate_email(email, check_deliverability=is_new_account)
                    validation.email
                    send_mail(
                    subject=f'Newsletter Vittoria Ecommerce',
                    message=f'Hi {email}  Thanks for subscribing to our Newsletter, \n The Vittoria Ecommerce Team',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email]) #this email account receives the damage claim notification
                    news.emails = email
                    news.save()
                    messages.info(request,'Thank you for subscribing to our Newsletter')
                except EmailNotValidError:
                    messages.error(request,"Sorry your email is not valid")

    return{'newsform':news}