from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from myapp.models import Client, Project, Sector
from myapp.serializers import ClientSerializer, ProjectSerializer, SectorSerializer

from myapp.serializers import CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView


# CUSTOM TOKEN VIEW
class CustomTokenObtainPairView(TokenObtainPairView):
    # Custom token obtain pair view
    serializer_class = CustomTokenObtainPairSerializer


# Client list viewset 
class ClientViewSet(viewsets.ModelViewSet):
    # Token authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Client's project viewset
class ClientProjectViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    # Token authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProjectSerializer

    def get_queryset(self):
        client_id = self.kwargs['client_pk']
        return Project.objects.filter(client_name_id=client_id)


# Sector list viewset
class SectorViewSet(viewsets.ModelViewSet):
    # Token authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

# Sector's project viewset
class SectorProjectViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    # Token authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        sector_id = self.kwargs['sector_pk']
        return Project.objects.filter(sector_id=sector_id)


# Project viewset
class ProjectViewSet(viewsets.ModelViewSet):
    # Token authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer