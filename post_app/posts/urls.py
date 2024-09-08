from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),  # List all posts and create new post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Retrieve a single post by ID
    path('posts/<int:post_id>/comment/', CommentCreateView.as_view(), name='post-comment'),  # Add comment to a post
]
