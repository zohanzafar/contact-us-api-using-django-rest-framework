from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=55)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
