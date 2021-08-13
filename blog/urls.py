from django.urls import path

from .views import *

app_name = 'blog'
urlpatterns = [
    path('', blog, name='index'),
    path('create/', create, name='create'),
    path('category/<str:inputKat>/', category, name='category'),
    path('artikel/<slug:inputSlug>/', artikel, name='artikel'),
]
