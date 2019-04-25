from django.db import models

# Create your models here.
class Chat(models.Model) :

    sender = models.CharField(max_length= 20, default='unknown')
    receiver = models.CharField(max_length= 20, default='unknown')
    room_name = models.CharField(max_length = 200, default='')
    text = models.CharField(max_length = 200, default='')

    def __str__(self) :
        return self.room_name + " - " + self.text