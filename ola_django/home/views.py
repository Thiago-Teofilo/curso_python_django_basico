from django.shortcuts import render

def home(request):

    context = {
        'text': 'Estamos na home',
    }

    return render(
        request,
        'home/index.html',
        context
    )