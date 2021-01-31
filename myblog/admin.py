from django.contrib import admin
from .models import BlogPost, Categories
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Categories)
