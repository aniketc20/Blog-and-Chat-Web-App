from Account.models import Account
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
    likes = models.ManyToManyField(Account, related_name='blog_post')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.author, self.post)

'''class BestComment(models.Model):
    blog = models.OneToOneField(BlogPost, on_delete=models.PROTECT)
    comment = models.ForeignKey(Comment, on_delete=models.PROTECT)'''
