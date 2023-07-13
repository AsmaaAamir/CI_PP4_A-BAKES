from .models import Comment, Post
from django import forms


class AddPostFrom(forms.ModelForm):
    """
    Form to allow user to add recipes
    """
    class Meta:
        Modle = Post
        fields = ('title', 'featured_image', 'excerpt', 'ingredient_content', 'featured_image2', 'insuturction_content', 'featuren_image3')


class CommentForm(forms.ModelForm):
    """
    created form so user can add comment via this form 
    """
    class Meta:
        model = Comment
        fields = ('body',)