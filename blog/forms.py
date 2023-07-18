# Import
# 3rd party:
# ----------------------------------------------------------
from django import forms
from django_summernote.widgets import SummernoteWidget

# Internal:
# ------------------------------------
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    """
    created form so user can share their recipe
    """

    class Meta:
        """
        Stating the meta characteristise of adding post form
        """
        model = Post
        fields = (
            "title",
            "featured_image",
            "author",
            "excerpt",
            "ingredient",
            "featured_image2",
            "instruction",
            "featured_image3",
        )
        widgets = {
            "body": SummernoteWidget(),
        }


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
