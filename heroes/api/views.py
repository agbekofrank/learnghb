from rest_framework.viewsets import generics
from rest_framework import permissions, authentication
from .serializers import HeroSerializer, SlipSerializer
from ..models import Hero, Slip

class HeroListAPIView(generics.ListAPIView):

    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [permissions.IsAuthenticated]


class HeroCreateAPIView(generics.CreateAPIView):

    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class HeroDetailAPIView(generics.RetrieveAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class HeroUpdateAPIView(generics.UpdateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class HeroDestroyAPIView(generics.DestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class SlipListCreateAPIView(generics.ListCreateAPIView):
    queryset = Slip.objects.all()
    serializer_class = SlipSerializer

