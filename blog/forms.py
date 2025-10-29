from django import forms
from .models import Post, Comment


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Your name'})
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", 'placeholder': 'Your comment here...'})
    )