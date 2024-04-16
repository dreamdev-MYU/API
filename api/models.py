from django.db import models
from django.contrib.auth.models import AbstractUser

KOKAND, FERGHANA, ANDIJAN = 'kokand', 'ferghana', 'andijan'

class Student(AbstractUser):

    LOCATION_TYPE_CHOISE = (
        (KOKAND, KOKAND),
        (FERGHANA, FERGHANA),
        (ANDIJAN, ANDIJAN),
    )


    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    photo = models.ImageField(upload_to='users_photo/', default='users_photo/default.jpg') 
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True)
    location = models.CharField(max_length=20, choices=LOCATION_TYPE_CHOISE)
    major = models.CharField(max_length=100, null=True, blank=True)
    