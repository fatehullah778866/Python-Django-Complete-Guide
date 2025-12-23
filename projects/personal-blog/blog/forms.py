from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Form for creating and editing blog posts."""

    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Write your post content', 'rows': 8}
            ),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author name'}),
        }

