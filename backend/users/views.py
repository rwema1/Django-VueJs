from .models import User
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

#REGISTER VIEW
class RegisterView(APIView):
    authentication_classes = []  # No authentication required
    permission_classes = [AllowAny]  # Allow any user to access this view

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(serializer.data)

#LOGIN VIEW
class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Validate email and password
        if not email or not password:
            raise AuthenticationFailed('Email and password are required.', code='invalid_credentials')

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User with this email does not exist.', code='invalid_user')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password.', code='invalid_password')

        # Generate token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Return token in response
        return Response({'token': access_token})

#LOGOUT VIEW
class LogoutView(APIView):
    authentication_classes = []
    
    def post(self, request):
        try:
            # Get refresh token from request header
            refresh_token = request.headers.get('Authorization').split()[1]
            
            # Blacklist the refresh token to invalidate it
            RefreshToken(refresh_token).blacklist()
            
            return Response({'detail': 'Successfully logged out.'})
        except Exception as e:
            return Response({'detail': 'Failed to logout.', 'error': str(e)})

#User data view
class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)