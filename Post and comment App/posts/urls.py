
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.post_list_view, name='post_list'),
    path('post/create/', views.create_post_view, name='create_post'),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('post/<int:pk>/edit/', views.update_post_view, name='update_post'),
    path('post/<int:pk>/delete/', views.delete_post_view, name='delete_post'),
]
