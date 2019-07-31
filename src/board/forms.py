from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = [
            'subject'
        ]

    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput()
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'content'
        ]

    name = forms.CharField(
        label='Name',
        required=False,
        widget=forms.TextInput()
    )
    content = forms.CharField(
        widget=forms.Textarea()
    )
