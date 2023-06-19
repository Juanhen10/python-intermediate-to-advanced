from django.urls import path
from home import views

#  HTTP Request <-> HTTP Response
# MTV (MVC) - mode view tamplate
app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]
