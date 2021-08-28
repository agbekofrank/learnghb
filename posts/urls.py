from django.urls import path, include
from .views import *

urlpatterns = [
    path('', posts_list, name='list'),
    path('create/', posts_create, name='create'),
    path('<str:slug>/', post_detail, name='detail'),
    path('<str:slug>/edit/', posts_update, name='update'),
    path('<str:slug>/delete/', posts_delete),
]
app_name = 'posts'