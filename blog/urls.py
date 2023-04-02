from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('blog', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='recipe'),
    path('login', views.LoginPage.as_view(), name='login'),
    path('logout', views.LogoutPage.as_view(), name='logout'),
    path('signup', views.SignupPage.as_view(), name='signup'),
   
]