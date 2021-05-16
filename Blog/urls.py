"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myblog.models import Categories

from Account.views import (
    login_view,
    registration_view,
    logout_view,
    dashboard
)
from myblog.views import (
    home,
    category_view,
    create_blog,
    blog_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logout_view, name="logout"),
    path('create_blog/', create_blog, name="create_blog"),
    path('category/<str:cats>', category_view, name="category"),
    path('category/<str:cats>/details', blog_view, name="blog_view")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
