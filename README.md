# contact-us-api-using-django-rest-framework

This project implements a **Contact Us API** using Django and Django REST Framework. The API accepts a form submission with the following fields: 

{ 
    `first_name`, 
    `last_name`, 
    `email`, 
    `phone`,
    `message`
} 

and sends the form data to an admin via email. The project uses `python-decouple` to manage sensitive data like the secret key and email credentials securely.

## Project Setup

Follow these steps to set up and run the project.

```bash
### 1. Clone the Repository

git clone https://github.com/your-username/contact-us-api.git
cd contact-us-api

### 2. Create and Activate a Virtual Environment

Linux:

python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies

pip install django
pip install djangorestframework
pip install python-decouple

### 4. Set Up Environment Variables

SECRET_KEY='your-secret-key'
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_sender_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=your_sender_email@gmail.com
ADMIN_EMAIL=admin@example.com

### 4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

### 5. Create a Superuser (Admin)

python manage.py createsuperuser

### 6. Run the Development Server
  
python manage.py runserver

### 6. API Usage

Endpoint: /api/v1/contact-us/
Method: POST
Submit a contact form using a POST request with the following fields:

first_name: User's first name.
last_name: User's last name.
email: A valid email address.
phone: Phone number.
message: Message content (must be between 10 and 255 characters).

### Request Body Example:

json:
{
    "first_name": "Zohan",
    "last_name": "Zafar",
    "email": "zohanzafar@example.com",
    "phone": "+923512489512",
    "message": "This is a test message."
}

### Success Response Example:

json:
{
    "message": "Contact form submitted successfully!"
}

### Error Response Example:

json:
{
    "email": ["Invalid email domain."],
    "message": ["Message should be between 10 and 255 characters long."]
}

### Throttling Configuration (in settings.py):

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',  # Throttling for anonymous users
        'rest_framework.throttling.UserRateThrottle',  # Throttling for authenticated users
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/day',  # Throttling for anonymous users can make 2 requests per day
        'user': '5/day',  # Throttling for authenticated users can make 5 requests per day
    }
}

You can set the congfiguration as per your requirements.

### Exceeding Throttling Limits (Example Error Response):

json:
{
    "detail": "Request was throttled. Expected available in 86400 seconds."
}

### License
This `README.md` contains clear instructions for setting up the project, creating the virtual environment, installing dependencies, handling sensitive information with `python-decouple`, and running the server. It also includes details on API usage, throttling, and migration steps.
