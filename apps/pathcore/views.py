from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Corepath
from .models import CoreUser
from .models import SubCorePath
from .serializers import SerializerCore  # noqa: F401
from .serializers import SerializerCoreU  # noqa: F401
from .serializers import SerializerSubCore  # noqa: F401

# Create your views here.


class ViewCreateCore(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        serializer = SerializerCore(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class ViewListCore(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        core = Corepath.objects.filter(status_delete=False)
        serializer = SerializerCore(core, many=True)
        return Response(serializer.data)


class ViewUpdateCore(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        core = Corepath.objects.get(pk=pk)
        serializer = SerializerCore(core, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class ViewDeleteCore(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        core = Corepath.objects.get(pk=pk)
        core.status_delete = True
        core.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ViewCreateSubCore(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        serializer = SerializerSubCore(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class ViewListSubCore(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        core = SubCorePath.objects.filter(status_delete=False)
        serializer = SerializerSubCore(core, many=True)
        return Response(serializer.data)


class ViewUpdateSubCore(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        core = SubCorePath.objects.get(pk=pk)
        serializer = SerializerSubCore(core, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class ViewDeleteSubCore(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        core = SubCorePath.objects.get(pk=pk)
        core.status_delete = True
        core.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ViewCoreUser(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        serializer = SerializerCoreU(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        core_list = CoreUser.objects.filter(
            user_id=request.user,
            status_delete=False,
        )
        serializer = SerializerCoreU(core_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ViewCoreUserUpdate(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        core_user = CoreUser.objects.get(pk=pk)
        serializer = SerializerCoreU(core_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class ViewDeleteUserCore(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (IsAuthenticated,)

    def delete(self, reuqest, pk):
        core_user = CoreUser.objects.get(pk=pk)
        core_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
