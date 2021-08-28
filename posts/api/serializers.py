from rest_framework.serializers import (
    ModelSerializer, HyperlinkedIdentityField,
    SerializerMethodField, ImageField
    )
from posts.models import Post
from accounts.api.serializers import UserSerializer
from .image_decoder import Base64ImageField

class PostCreateSerializer(ModelSerializer):
    # image = Base64ImageField(max_length=None, required=False)
    # image = SerializerMethodField(required=False)
    image = ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'draft', 'publish_date']

        def get_image(self, img):
            try:
                image = img
            except:
                image = None
            return image

class PostEditSerializer(ModelSerializer):
    image = ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = Post
        fields = '__all__'
    

class PostDetailSerializer(ModelSerializer):
    # user = SerializerMethodField()
    user = UserSerializer(read_only=True)
    image = SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'
    
    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, img):
        try:
            image = 'http://localhost:8000' + img.image.url
        except:
            image = None
        return image

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
    )
    user = SerializerMethodField()
    delete_url = HyperlinkedIdentityField(
        view_name='posts-api:delete',
        lookup_field='pk'
    )
    # image_url = HyperlinkedIdentityField()
    class Meta:
        model = Post
        fields = [
            'url', 'user', 'title', 'image', 'content',
            'delete_url','slug', 'timestamp', 'publish_date'
            ]

    def get_user(self, obj):
        return str(obj.user.username)
        