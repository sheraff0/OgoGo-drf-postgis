from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from contrib.users.models import OTP
from .serializers import LoginSerializer, RegisterSerializer, OTPSerializer, OTPVerifySerializer


class LoginView(APIView):
    """
    Login with username | email and password
    """
    permission_classes = []
    http_method_names = ['post']
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=200)
        except:
            return Response({"errors": {"details": ["Bad credentials"]}}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    """
    Login with username | email and password
    """
    permission_classes = []
    http_method_names = ['post']
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


class OTPViewSet(GenericViewSet):
    permission_classes = []
    pagination_class = None
    http_method_names = ["post"]

    def get_serializer_class(self):
        if self.action == "verify":
            return OTPVerifySerializer
        return OTPSerializer

    @action(detail=False, methods=["post"])
    def obtain(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({"message": "ok"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def verify(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
