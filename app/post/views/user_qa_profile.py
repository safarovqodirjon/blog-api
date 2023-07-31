from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from ..models import UserQAProfile
from ..serializers import UserQAProfileSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserQAProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserQAProfile.objects.all()
    serializer_class = UserQAProfileSerializer

    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserQAProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserQAProfile.objects.all()
    serializer_class = UserQAProfileSerializer
    lookup_field = 'pk'
