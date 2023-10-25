# Imports
# 3rd party:
# ---------------------
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import FormView
from django.utils.text import slugify
from django.contrib.messages.views import SuccessMessageMixin


# Internal:
# --------------------
from .models import Post
from .forms import AddPostForm, CommentForm


# Create your views here.


class HomePage(ListView):
    """
    class-based function so the home page
    can be displayed.
    """
    def get(self, request):
        return render(request, 'index.html')


class PostList(ListView):
    """
    class-based view to list of recipes that have been posted
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6


class PostDetail(ListView):

    def get(self, request, slug, *args, **kwargs):
        """
        Views the selected recipe from the blog page
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Comment section in each post, so user can see the posted Comments that
        have been approved by the admin
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class AddPost(ListView):
    """
    user can add recipe 
    """
    model = Post
    form_class = AddPostForm
    template_name = "addpost.html"

    def post(self, request, *args, **kwargs):
        form = AddPostForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.slug = slugify(form.title)
            form.save()
            messages.success(request, 'Thank you for sharing your recipe')
        return redirect(reverse('blog'))

    def get(self, request, *args, **kwargs):

        form = AddPostForm()

        return render(request, 'addpost.html', {"form": form})


class EditPost(ListView):
    """
    User can edit their current post 
    """
    def get(self, request):
        return render(request, 'editpost.html')


class DeletePost(ListView):
    """
    User can delete their current post d
    """
    def get(self, request):
        return render(request, 'deletepost.html')


class PostLike(ListView):
    """
    user can view number of likes on a posts
    """
    def post(self, request, slug):
        """
        aLlowing user to like post and advise if they have
        already liked the post.
        """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe', args=[slug]))


class LoginPage(ListView):
    """
    Login page can be viewed
    """
    def get(self, request):
        return render(request, 'login.html')


class LogoutPage(ListView):
    """
    Logout Page  can be viewed
    """
    def get(self, request):
        return render(request, 'logout.html')


class SignupPage(ListView):
    """
    Sign up page can be viewed
    """
    def get(self, request):
        return render(request, 'signup.html')


class GallaryPage(ListView):
    """
    Gallary  page can be viewed
    """
    def get(self, request):
        return render(request, 'gallary.html')


class ContactPage(ListView):
    """
    Contact Page  can be viewed
    """
    def get(self, request):
        return render(request, 'contact.html')
