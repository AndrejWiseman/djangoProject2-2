from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Naslov'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sadrzaj'})
        }

    def clean(self):
        data = self.cleaned_data

        return data
