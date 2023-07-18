# Import
# 3rd party:
# ----------------------------------------------------------
from django import forms
from django_summernote.widgets import SummernoteWidget

# Internal:
# ------------------------------------
from .models import Post, Comment




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
