from django.shortcuts import render

# Create your views here.

context = {
    'text': 'ola home'
}


def home(request):
    print('home')
    return render(
        request, 'home/index.html',
        context

    )
