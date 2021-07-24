from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from Account.models import Account
from .models import BlogPost, Categories, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
from .forms import BlogForm
# Create your views here.

def home(request):
    query_set = BlogPost.objects.all()
    paginator = Paginator(query_set, 2)
    page_req_var = 'page'
    page = request.GET.get(page_req_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    categories = Categories.objects.all()
    context = {}
    context['blog'] = paginated_queryset
    context['categories'] = categories
    context['page'] = page_req_var
    if request.is_ajax():
        card_text = request.POST.get('text')
        cat = BlogPost.objects.filter(categories=card_text).values_list()
        return JsonResponse({'data': list(cat)})
    print(context['blog'])
    return render(request, "home.html", context)

def category_view(request, cats):
    context={}
    categories = Categories.objects.all()
    context['categories'] = categories
    query_set = BlogPost.objects.filter(categories=cats)
    paginator = Paginator(query_set, 2)
    page_req_var = 'page'
    page = request.GET.get(page_req_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context['blog'] = paginated_queryset
    context['page'] = page_req_var
    return render(request, "home.html", context)

def create_blog(request):
    user = request.user
    context = {}
    cat = Categories.objects.all()
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        category=form.cleaned_data['categories']
        author = Account.objects.filter(first_name=user.first_name).first()
        obj.author = author
        # IMP CONCEPT we need to initially save the model before
        # we can use the id of the model to save the category
        obj.save() 
        obj.categories.set(category)
        return redirect('home')
    if user.is_authenticated:
        form = BlogForm()
        context['blog_form'] = form
        context['categories'] = cat
        return render(request, "create_blog.html", context)
    return redirect("login")

def blog_view(request, pk):
    context = {}
    blog = BlogPost.objects.get(id=pk)
    cat = Categories.objects.all()
    comments = Comment.objects.filter(post=blog)
    context['blog'] = blog
    context['categories'] = cat
    context['comments'] = comments
    if request.method=='POST':
        if 'comment' in request.POST:
            comment = request.POST.get('comment')
            Comment.objects.create(body=comment, author=request.user, post=blog)
            return JsonResponse({'comment': comment})
        if 'like' in request.POST:
            users= blog.likes.all()
            if(request.user in users):
                blog.likes.remove(request.user)
                return JsonResponse({'likes': users})
            else:
                blog.likes.add(request.user)
                return JsonResponse({'likes': users})
    return render(request, "Blog_view.html", context)

def chat(request, room):
    return render(request, "chat.html", {'room': room})