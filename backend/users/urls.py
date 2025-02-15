from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserDetailView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view(), name='logout'),
    path('user', UserDetailView.as_view(), name='user-detail'),
]