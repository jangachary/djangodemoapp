from django.db import models



class MyModel(models.Model):
    ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('user', 'User'),
    # Add other roles as needed
]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,default=None)
    email = models.EmailField()
    # Add other fields as needed
