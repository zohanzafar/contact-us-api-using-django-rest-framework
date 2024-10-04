# contact/utils.py
from django.core.mail import send_mail
from django.conf import settings
from decouple import config

def send_contact_email(data):
    subject = f"New Contact Us Message from {data['first_name']} {data['last_name']}"
    message = (
        f"First Name: {data['first_name']}\n"
        f"Last Name: {data['last_name']}\n"
        f"Email: {data['email']}\n"
        f"Phone Number: {data['phone']}\n"
        f"Message: {data['message']}\n"
    )
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_email = settings.ADMIN_EMAIL  

    send_mail(
        subject,
        message,
        sender_email,
        [recipient_email], 
        fail_silently=False,
    )
