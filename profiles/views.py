from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    PasswordResetRequestSerializer,
    CustomTokenObtainPairSerializer
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        response_data = UserSerializer(user).data
        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)

        if hasattr(request.user, 'auth_token'):
            request.user.auth_token.delete()

        return Response({
            "status": "success",
            "message": "Muvaffaqiyatli tizimdan chiqildi"
        }, status=status.HTTP_200_OK)

    def get(self, request):
        return Response({
            "error": "GET metodi qo'llab-quvvatlanmaydi. Iltimos, POST metodidan foydalaning"
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = UserProfile.objects.get(email=email)

            reset_link = f"http://your-frontend-domain.com/reset-password/{user.id}/"

            send_mail(
                subject="Parolni tiklash",
                message=f"Parolni tiklash uchun ushbu havolani bosing: {reset_link}",
                from_email="noreply@yourdomain.com",
                recipient_list=[email],
            )
            return Response({"message": "Parolni tiklash havolasi emailingizga yuborildi."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)