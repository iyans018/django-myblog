from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home Page',
        'header': 'Oktavian Aji Tyas Azis'
    }

    return render(request, 'home.html', context)
