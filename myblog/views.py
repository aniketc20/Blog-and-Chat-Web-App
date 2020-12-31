from django.shortcuts import render
from .models import BlogPost
# Create your views here.

def home(request):
    query_set = BlogPost.objects.all()
    context = {}
    context['blog'] = query_set
    return render(request, "home.html", context)
