from rest_framework import status
from rest_framework.generics import (RetrieveDestroyAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from contrib.users.models import User
from contrib.users.serializers import UserSerializer


class UserViewSet(RetrieveUpdateAPIView, RetrieveDestroyAPIView):

    permission_classes = [IsAuthenticated,]
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch', 'delete']
    parser_classes = [MultiPartParser]

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            request.user, 
            data=request.data, 
            partial=True
        )
        serializer.context.update({"user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request):
        user = User.objects.get(id=request.user.id)
        if user:
            user.is_active = False
            user.save()
            return Response({"detail":'delete_success'}, status=status.HTTP_200_OK)
        else:
            return Response({"detail":'user_not_exist'}, status=status.HTTP_404_NOT_FOUND)   

