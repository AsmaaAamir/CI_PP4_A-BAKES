# Imports
# 3rd party:
# ---------------------
from django.test import TestCase


# Internal:
# --------------------
from .forms import AddPostForm, CommentForm


class AddPostFormTest(TestCase):
    """
        Add Post test
    """
    def test_addpot_valid(self):
        """
        Testing id the add test form is valid
        """
        form = AddPostForm(data={
            "title": "testtitle",
            "excerpt": "testtext",
            "ingredient_content": "testingredient",
            "instruction_content": "testinstruction",
        })
        self.assertTrue(form.is_valid())
