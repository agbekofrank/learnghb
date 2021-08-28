from rest_framework import serializers
from ..models import Hero, Slip

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'

class SlipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slip
        fields = '__all__'