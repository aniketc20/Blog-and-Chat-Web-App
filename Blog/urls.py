from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from myblog.models import Categories
from django_email_verification import urls as mail_urls

from Account.views import (
    login_view,
    registration_view,
    logout_view,
    dashboard,
)
from myblog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('email/', include(mail_urls)),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logout_view, name="logout"),
    path('create_blog/', create_blog, name="create_blog"),
    path('category/<str:cats>', category_view, name="category"),
    path('category/<str:pk>/details', blog_view, name="blog_view"),
    path('<str:room>/', chat, name="room"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
