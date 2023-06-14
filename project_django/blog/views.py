from django.shortcuts import render

# Create your views here.


def blog(request):
    context = {
        'text': 'ola blog'
    }
    return render(
        request,
        'blog/index.html',
        context
    )


def exemplo(request):
    context = {
        'text': 'ola exemplo',
        'title': 'Essa é uma página de exemplo'
    }
    return render(
        request,
        'blog/exemplo.html',
        context

    )
