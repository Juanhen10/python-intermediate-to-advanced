from django.urls import path
from home import views

#  HTTP Request <-> HTTP Response
# MTV (MVC) - mode view tamplate

urlpatterns = [
    path('', views.home),
]
