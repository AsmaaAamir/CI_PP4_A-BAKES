# Import
# 3rd party:
# ----------------------------------------------------------
from django import forms

# Internal:
# ------------------------------------
from .models import Post, Comment

class AddPostForm(forms.ModelForm):
    title = forms.CharField(required=True)
    body = forms.CharField(required=True)

    class Meta:
        model = Post
        fields = ('title', 'body',)


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
