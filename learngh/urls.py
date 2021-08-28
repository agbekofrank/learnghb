"""learngh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts import views, urls
import accounts.urls
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts.urls, namespace='accounts')),

    # rest jwt and allauth

    # path('api/auth/login/', obtain_jwt_token),
    # path('api/token/refresh/', refresh_jwt_token),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/signup/', include('rest_auth.registration.urls')),
    path('api/auth/refresh-token/', refresh_jwt_token),

    # auth users
    path('api/users/', include('accounts.api.urls', namespace='users-api')),
    
    # posts api views 
    path('posts/api/', include('posts.api.urls', namespace='posts-api')),
    path('', include(urls, namespace="posts")),

    # heroes
    path('heroes/api/', include('heroes.api.urls', namespace='heroes-api')),

    # file upload 
    # path('files/api/', include('file_upload.api.urls', namespace='files-api'))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)