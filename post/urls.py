from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name= "home_view"),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('search/', views.search_posts, name= 'search_posts'),
    path('post/<int:blog_id>', views.post_view, name='post'),
    path('category/<str:foo>/', views.category_posts, name='category'),
]