from django.db import models
from django.conf import settings


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    image = models.ImageField()
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Date Published')
    date_up = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    # author establishes rel between user(author) and blog post
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
