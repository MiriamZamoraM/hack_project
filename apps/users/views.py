from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserLoginSerializar
from .serializers import UserSerializer
from lib.auth import get_token
from lib.exceptions import TokenException


class RegistryView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    """
        - Registry
            Input should be in the format:
            {"name":"John","email": "johnm@email.com", "password": "1234abcd"}
            """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = get_token(request.data["email"], request.data["password"])
            data = {
                "id": serializer.data["id"],
                "email": serializer.data["email"],
                "auth": token.json(),
            }
            return Response(status=status.HTTP_201_CREATED, data=data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        - User Login
        Gets tokens with email and password. Input should be in the format:
        {"email": "email@email.com", "password": "1234abcd"}
        """
        serializer = UserLoginSerializar(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=request.data["email"])
            try:
                token = get_token(request.data["email"], request.data["password"])
                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "user_id": user.id,
                        "email": user.email,
                        "auth": token.json(),
                    },
                )

            except User.DoesNotExist:
                return Response(
                    {"message": "No existe un usuario con ese correo"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            except TokenException:
                return Response(
                    {"message": "Error al generar token"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class RefreshTokenView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        Rrefresh token. Input should be in the format:
        {"refresh_token": "<token>"}
        """
        token = get_token(request.data["email"], request.data["password"])

        return Response(token.json())
