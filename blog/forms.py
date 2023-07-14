# Import
# 3rd party:
# ------------------------
from django import forms

# Internal:
# ---------------------------
from .models import Comment, Post


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
