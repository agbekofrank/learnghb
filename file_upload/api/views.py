from .serializers import FileUploadSerializer
from rest_framework import views, parsers, response, status, generics
from ..models import File

class FileUploadAPICreateView(views.APIView):

    parser_classes = (parsers.MultiPartParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return response.Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUploadAPIListView(generics.ListAPIView):

    queryset = File.objects.all().order_by('-id')
    print(queryset)
    serializer_class = FileUploadSerializer