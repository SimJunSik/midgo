from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser) :

    USER_GRADE_CHOICES = {
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold')
    }

    name = models.CharField(blank=True, max_length=255, default='')
    phone = models.CharField(max_length=40, null=True)
    addr = models.CharField(max_length=100, null=True)
    check_notification =  models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length = 30, choices = USER_GRADE_CHOICES, null=True)
    is_recognized = models.CharField(max_length=40,default='in_progress')
    

class Cat(models.Model) :

    image = models.ImageField(null=True, blank=True, upload_to='catImage/')
    name = models.CharField(max_length = 20, default='unknown')
    gender = models.CharField(max_length = 10, default='unknown')
    birth = models.CharField(max_length=20, default='unknown')
    age = models.CharField(max_length = 10,default='0')
    breed = models.CharField(max_length = 50, default='unknown')
    owner = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='cats')
    eatinghabit= models.TextField(default='')
    health= models.TextField(default='')
    route=models.TextField(default='')
    meet=models.TextField(default='')
    is_recognized = models.CharField(max_length=40,default='in_progress')

    def __str__(self) :
        return self.owner.username + " - " + self.name

class Article(models.Model) :

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='articles')
    title = models.CharField(max_length = 100, default='')
    content = models.TextField()

    def __str__(self) :
        return self.title + " - " + str(self.creator.username)

class ArticleImage(models.Model) :

    file = models.ImageField(upload_to='articleImage/')
    article = models.ForeignKey(Article, on_delete = models.CASCADE, null=True, blank=True, related_name='articleImages')

    def __str__(self) :
        return self.article.title

class Notification(models.Model) :

    CATEGORY_CHOICES = {
        ('reply', 'Reply'),
        ('notice', 'Notice')
    }

    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    category = models.CharField(max_length = 30, choices=CATEGORY_CHOICES, null=True )
    creator = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='create_notifications')
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='receive_notifications')
    is_checked = models.BooleanField(default=False)
    article = models.ForeignKey(Article, on_delete = models.CASCADE, null=True, blank=True, related_name='article_notifications')
    # reply = models.ForeignKey(Reply, on_delete = models.CASCADE, null=True, blank=True, related_name='reply_notifications')

    def __str__(self) :
        return self.category + " - " + str(self.created_at)


class SummerNoteImage(models.Model) :

    file = models.ImageField(upload_to='summernoteImage/')
    url = models.TextField(default='', null=True, blank=True)
