from django.urls import path
from .views import register, login_view, logout_view, task_list, add_task, edit_task, remove_task, toggle_task, profile
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='tasks/', permanent=False)),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/add/', add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('tasks/remove/<int:task_id>/', remove_task, name='remove_task'),
    path('tasks/toggle/<int:task_id>/', toggle_task, name='toggle_task'),
    path('profile/', profile, name='profile'),
]
