from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, SectorViewSet, ProjectViewSet, ClientProjectViewSet, SectorProjectViewSet

from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
#API Routes
router = DefaultRouter()

router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'clients/(?P<client_pk>\d+)/projects', ClientProjectViewSet, basename='client-projects')
router.register(r'sectors', SectorViewSet, basename='sectors')
router.register(r'sectors/(?P<sector_pk>\d+)/projects', SectorProjectViewSet, basename='sector-projects')
router.register(r'projects', ProjectViewSet, basename='projects')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('users.urls')),
]
#adding API routes to URLS
urlpatterns += router.urls