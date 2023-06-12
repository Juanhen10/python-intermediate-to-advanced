from django.shortcuts import render

# Create your views here.


def home(request):
    print('home')
    return render(
        request, 'home/index.html')
