from .models import Comment, Post
from django import forms


class AddPostFrom(forms.ModelForm):
    """
    Form to allow user to add recipes
    """
    



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)