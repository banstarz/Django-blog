from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Название статьи',
            }),
            'anons': TextInput(attrs={
                'placeholder': 'Анонс статьи',
            }),
            'full_text': Textarea(attrs={
                'placeholder': 'Текст статьи',
            }),
            'date': DateTimeInput(attrs={
                'placeholder': 'Дата публикации',
            }),

        }