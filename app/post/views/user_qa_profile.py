from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from ..models import UserQAProfile
from ..serializers import UserQAProfileSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class IsSuperUserOrReadOnly(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in ["PUT", "PATCH", "POST", "DELETE"]:
            return request.user.is_superuser
        return True


class UserQAProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserQAProfile.objects.all()
    serializer_class = UserQAProfileSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]


class UserQAProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserQAProfile.objects.all()
    serializer_class = UserQAProfileSerializer
    lookup_field = 'pk'
