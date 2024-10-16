from django.core.mail import send_mail
from django.conf import settings

def send_contact_email(data):
    subject = f"Subject: {data['subject']} - {data['name']}"
    message = (
        f"Name: {data['name']}\n"
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
