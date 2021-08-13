from django import forms
from .models import ArtikelModel


class ArtikelForm(forms.ModelForm):

    class Meta:
        model = ArtikelModel
        fields = (
            "title",
            "body",
            "category",
            "author",
        )

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'masukan judul artikel',
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'masukan isi artikel',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'masukan nama pembuat',
                }
            ),
        }
