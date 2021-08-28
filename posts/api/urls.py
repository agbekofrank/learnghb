from django.urls import path
from .views import (
    PostListAPIView, PostDetailAPIView,
    PostDestroyAPIView, PostUpdateAPIView,
    PostCreateAPIView, PostEditAPIView
)

urlpatterns = [
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<str:slug>/', PostDetailAPIView.as_view(), name='detail'),
    path('<str:slug>/edit/', PostEditAPIView.as_view(), name='edit'),
    # path('<str:slug>/update/', PostUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDestroyAPIView.as_view(), name='delete'),
    path('', PostListAPIView.as_view(), name='list'),
]
app_name = 'posts'