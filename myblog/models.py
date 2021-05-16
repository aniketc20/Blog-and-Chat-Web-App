from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class Categories(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    categories = models.ManyToManyField(Categories)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to = '')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Date Published')
    date_up = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    # author establishes rel between user(author) and blog post
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
