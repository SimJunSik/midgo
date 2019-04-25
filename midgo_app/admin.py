from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Cat)
admin.site.register(Notification)
admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(SummerNoteImage)