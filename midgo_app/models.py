from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser) :

    pass

class Cat(models.Model) :

    name = models.CharField(max_length = 20, default='unknown')
    age = models.CharField(max_length = 10,default='0')
    breed = models.CharField(max_length = 50, default='unknown')
    image = models.ImageField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='cats')

    def __str__(self) :
        return self.owner.username + " - " + self.name