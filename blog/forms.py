# Import
# 3rd party:
# ----------------------------------------------------------
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget

# Internal:
# ------------------------------------
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    """
    created form so user can share recipes via this form
    """
    title = forms.CharField(required=True)
    excerpt = forms.CharField(required=True)
    featured_image = forms.ImageField
    ingredient_content = forms.CharField(required=True)
    instruction_content = forms.CharField(required=True)

    class Meta:
        """
        defines post form meta include
        """
        model = Post
        fields = ('title', 'excerpt', 'featured_image', 'ingredient_content', 'instruction_content')
        widgets = {
            'ingredient_content': SummernoteInplaceWidget(),
            'instruction_content': SummernoteInplaceWidget()
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
