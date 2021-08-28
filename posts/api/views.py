from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView,
    CreateAPIView, RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly,
    AllowAny, IsAdminUser
)
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    PostListSerializer, PostDetailSerializer,
    PostCreateSerializer, PostEditSerializer
    )
from rest_framework import parsers, mixins
from posts.models import Post

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            # data = serializer.validated_data
            # print(data)
            serializer.save(user=self.request.user)

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all() #.order_by('-id')
    serializer_class = PostListSerializer

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser]



class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostEditAPIView(
    mixins.DestroyModelMixin, mixins.UpdateModelMixin, RetrieveAPIView
    ):
    queryset = Post.objects.all()
    serializer_class = PostEditSerializer
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser]
    lookup_field = 'slug'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)