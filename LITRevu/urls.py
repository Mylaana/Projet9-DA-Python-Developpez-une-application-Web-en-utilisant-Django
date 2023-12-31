"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import blog.views
import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.index_page, name="index"),
    path('index/', authentication.views.index_page, name="index"),
    path('feed/', blog.views.feed_page, name="feed"),
    path('posts/', blog.views.posts_page, name="posts"),
    path('follower/', blog.views.follower_page, name="follower"),
    path('signup/', authentication.views.signup_page, name="signup"),
    path('log-out', authentication.views.log_out, name="log-out"),
    path('create-ticket/', blog.views.ticket_page, name='create-ticket'),
    path('create-ticket/<int:ticket_id>/', blog.views.ticket_page_update, name='create-ticket'),
    path('create-review/<int:ticket_id>', blog.views.review_page, name='create-review'),
    path('create-review/<int:ticket_id>/<int:review_id>', blog.views.review_page_update, name='create-review'),
    path('tickets-reviews/', blog.views.tickets_reviews_page, name='tickets-reviews'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
