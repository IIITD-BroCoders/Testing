from django.db import models

class user(models.Model):
    # user_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)