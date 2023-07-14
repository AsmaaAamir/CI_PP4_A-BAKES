# Import
# 3rd party:
# ------------------------
from django import forms

# Internal:
# ---------------------------
from .models import Comment, Post


class AddPostForm(forms.ModelForm):
    """
    Form to allow user to add recipes
    """
    excerpt = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '5'
    }))

    class Meta:
        """
        defines a recipe post form meta include
        """
        model = Post
        fields = ('title', 'featured_image', 'excerpt', 'ingredient_content', 'featured_image2', 'insuturction_content', 'featuren_image3')


class CommentForm(forms.ModelForm):
    """
    created form so user can add comment via this form
    """
    class Meta:
        """
        defines comments form meta include
        """
        model = Comment
        fields = ('body',)
