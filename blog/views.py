from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import CommentForm, AddPostFrom


# Create your views here.


class HomePage(generic.ListView):
    def get(self, request):
        return render(request, 'index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
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


class PostLike(View):
    """
    user can view number of likes on a posts
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user) 
        return HttpResponseRedirect(reverse('recipe', args=[slug]))


@login_required 
class AddPost(generic.ListView):
    """
    Adding a recipe to the list of post
    """
    def get(self, request):
        if request.method == 'POST':
            form = AddPostFrom(request.POST, request.FILES or None)

            if form.is_valid():
                data = form.save(commit=False)
                data.author = request.user
                data.save()
                messages.success(
                    request, 'Your recipe has been posted sucessfully. Thank you we cannot wait to try it !'
                )
                return redirect(reverse('PostList'))
            else: 
                form = AddPostFrom
            
            return render( 
                request, 'addpost.html', 
                {
                    'form': form,
                    'author': 'Add Post'}
            )
  

class LoginPage(generic.ListView):
    """
    Login page can be viewed
    """
    def get(self, request):
        return render(request, 'login.html')


class LogoutPage(generic.ListView):
    """
    Logout Page  can be viewed
    """
    def get(self, request):
        return render(request, 'logout.html')


class SignupPage(generic.ListView):
    """
    Sign up page can be viewed
    """
    def get(self, request):
        return render(request, 'signup.html')


class GallaryPage(generic.ListView):
    """
    Gallary  page can be viewed
    """
    def get(self, request):
        return render(request, 'gallary.html')


class ContactPage(generic.ListView):
    """
    Contact Page  can be viewed
    """
    def get(self, request):
        return render(request, 'contact.html')