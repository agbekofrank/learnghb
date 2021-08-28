from django.urls import path
from .views import FileUploadAPICreateView, FileUploadAPIListView

urlpatterns = [
    path('', FileUploadAPICreateView.as_view(), name='create'),
    path('list', FileUploadAPIListView.as_view(), name='list'),
]

app_name = 'file_upload'