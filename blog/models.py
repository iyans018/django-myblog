from django.db import models
from django.utils.text import slugify

# Create your models here.


class ArtikelModel(models.Model):
    title = models.CharField(max_length=250)
    thumbnail = models.ImageField(blank=True)
    body = models.TextField()
    category = models.CharField(
        max_length=250,
        choices=(
            ('Tutorial', 'Tutorial'),
            ('Opini', 'Opini'),
            ('Filsafat', 'Filsafat'),
            ('Politik', 'Politik'),
            ('Ekonomi', 'Ekonomi'),
            ('Pemrograman', 'Pemrograman'),
            ('Cyber Security', 'Cyber Security'),
        ),
        default='Tutorial'
    )
    author = models.CharField(max_length=250)
    publish = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title
