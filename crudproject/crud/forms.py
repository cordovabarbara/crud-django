from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full 768px; border border-black rounded px-3 py-2'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border border-black rounded px-3 py-2',
                'rows': 4
            })
        }
