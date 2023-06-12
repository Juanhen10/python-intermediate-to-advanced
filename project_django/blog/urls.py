from blog import views as blog_views
from django.contrib import admin
from django.urls import path

#  HTTP Request <-> HTTP Response
# MTV (MVC) - mode view tamplate

urlpatterns = [
    path('', blog_views.blog),
    path('exemplo/', blog_views.exemplo),
]
