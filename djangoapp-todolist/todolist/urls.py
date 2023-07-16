from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/edit/<int:pk>', views.post_edit, name='post_edit'), #<int:pk>
    path('post/completed/<int:pk>', views.post_completed, name='post_completed'), #<int:pk>
    path('post/delete/<int:pk>', views.post_delete, name='post_delete'), #<int:pk>
]