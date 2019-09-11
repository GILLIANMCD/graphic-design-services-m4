from django.db import models

# A Simple Contact Form

class Contact(models.Model):
    full_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.full_name
    
    