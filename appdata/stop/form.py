from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'blog' not in title:
            raise ValidationError('we only accept blog')
        return title

