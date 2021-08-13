from django.shortcuts import render, redirect

# Create your views here.
from .models import ArtikelModel
from .forms import ArtikelForm


def blog(request):
    data_artikel = ArtikelModel.objects.all()
    kategori = ArtikelModel.objects.values('category').distinct()

    context = {
        'title': 'Blog Page',
        'header': 'Blog Page',
        'artikel': data_artikel,
        'kategori': kategori,
    }

    return render(request, 'blog/index.html', context)


def create(request):
    form_artikel = ArtikelForm()

    if request.method == 'POST':
        form_artikel = ArtikelForm(request.POST)
        if form_artikel.is_valid():
            form_artikel.save()

            return redirect('blog:index')

    context = {
        'title': 'Create Artikel',
        'form': form_artikel,
    }

    return render(request, 'blog/create.html', context)


def category(request, inputKat):
    data_artikel = ArtikelModel.objects.filter(category=inputKat)
    kategori = ArtikelModel.objects.values('category').distinct()

    context = {
        'title': 'Blog Page',
        'header': 'Blog Page',
        'artikel': data_artikel,
        'kategori': kategori,
    }

    return render(request, 'blog/index.html', context)


def artikel(request, inputSlug):
    data_artikel = ArtikelModel.objects.get(slug=inputSlug)

    context = {
        'title': 'Blog Page',
        'header': 'Blog page',
        'artikel': data_artikel,
    }

    return render(request, 'blog/artikel.html', context)
