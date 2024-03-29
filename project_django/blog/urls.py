from blog import views as blog_views
from django.contrib import admin
from django.urls import path

#  HTTP Request <-> HTTP Response
# MTV (MVC) - mode view tamplate

app_name = 'blog'

urlpatterns = [
    path('post/', blog_views.blog, name='home'),
    path('post/<int:post_id>/', blog_views.post, name='post'),
    path('exemplo/', blog_views.exemplo, name='exemplo'),
]
