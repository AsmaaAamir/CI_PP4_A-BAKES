from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('blog', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='recipe'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('login', views.LoginPage.as_view(), name='login'),
    path('logout', views.LogoutPage.as_view(), name='logout'),
    path('signup', views.SignupPage.as_view(), name='signup'),
    path('gallary', views.GallaryPage.as_view(), name='gallary'),
    path('contacy', views.ContactPage.as_view(), name='contact'),

  

   
]