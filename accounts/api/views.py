from rest_framework import generics, permissions, parsers, renderers
from .serializers import UserCreateSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters


User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    # parser_classes = [renderers.TemplateHTMLRenderer]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            print('Its given by the user login view, ', new_data)
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
