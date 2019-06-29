from django import forms
from .models import Posts


class PostsModelForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


