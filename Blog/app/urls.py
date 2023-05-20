from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_posts.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.detail_post.as_view(), name='detail-post'),
    #path('create/', views.create, name='create-post'),
    path('create/', views.post.as_view(), name='create-post'),
    path('post/<int:pk>/updata', views.updata.as_view(), name='updata-post'),
    path('post/<int:pk>/delete', views.delete.as_view(), name='delete-post'),
    path('posts/<str:username>/', views.user_list_posts.as_view(), name='user-posts'),
    path('about', views.About, name='blog-about'),
]
