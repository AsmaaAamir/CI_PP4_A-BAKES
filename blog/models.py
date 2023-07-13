from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    This is class based function to created a recipe post
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    featured_image = CloudinaryField('image', default='blog_image')
    excerpt = models.TextField(blank=True)
    ingredient_content = models.TextField()
    featured_image2 = CloudinaryField('image2', default='blog_image')
    instruction_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image3 = CloudinaryField('images', default='blog_image')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        The recipe posts are listed in descending order by the date they were published. 
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        Return a string of the title of the recipes
        """
        return self.title

    def number_of_likes(self):
        """
        Shows the number if likes on the recipes 
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Class based fucntion for comment so user can add comment to post
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order of teh comemtn posted on recipes in acending order
        """
        ordering = ["created_on"]

    def __str__(self):
        """
        Return a string that shows the comment and its author 
        """
        return f"Comment {self.body} by {self.name}"
