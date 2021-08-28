from django.urls import path
from .views import (
    HeroCreateAPIView, HeroListAPIView, HeroDetailAPIView, HeroUpdateAPIView,
    HeroDestroyAPIView, SlipListCreateAPIView
    )

urlpatterns = [
    path('', HeroListAPIView.as_view(), name='list'),
    path('create', HeroCreateAPIView.as_view(), name='create'),
    path('<int:pk>', HeroDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/edit', HeroUpdateAPIView.as_view(), name='edit'),
    path('<int:pk>/delete', HeroDestroyAPIView.as_view(), name='delete'),
    path('slip', SlipListCreateAPIView.as_view(), name='slip')
]
app_name = 'heroes'