from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Leads(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    dob = models.DateField()
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) 

    #  CHOICES = (
    #     ('Youtube', 'Youtube')
    #     ('LinkedIN', 'LinkedIN')
    #     ('Blog', 'Blog')
    # )
    # phone = models.BooleanField(default=True)
    # source = models.CharField(choices=CHOICES, max_length=30)
    # profile_picture = models.ImageField(blank=True, null=True)
    # file = models.FileField(blank=True, null=True)
    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
