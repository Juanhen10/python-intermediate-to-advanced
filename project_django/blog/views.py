from django.shortcuts import render

# Create your views here.


def blog(request):
    return render(request, 'blog/index.html')


def exemplo(request):
    return render(request, 'blog/exemplo.html')
