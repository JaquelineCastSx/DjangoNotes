from django import forms
from .models import Note

#Formulario de una nota
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
