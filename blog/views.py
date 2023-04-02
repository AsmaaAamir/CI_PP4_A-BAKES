from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

# Create your views here.


class HomePage(generic.ListView):
    def get(self, request):
        return render(request, 'index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 
            "recipe.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            }
        )


class LoginPage(generic.ListView):
    def get(self, request):
        return render(request, 'login.html')


class LogoutPage(generic.ListView):
    def get(self, request):
        return render(request, 'logout.html')


class SignupPage(generic.ListView):
    def get(self, request):
        return render(request, 'signup.html')
