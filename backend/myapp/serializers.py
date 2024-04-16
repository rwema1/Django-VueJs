from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Client, Project, Sector

#client serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')

#sector serializer
class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ('__all__')

#project serializer    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')

#custom token serializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['id'] = user.id
        token['email'] = user.email
        token['email'] = user.name

        return token