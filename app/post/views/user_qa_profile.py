from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from ..models import UserQAProfile
from ..serializers import UserQAProfileSerializer


class UserQAProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserQAProfile.objects.all()
    serializer_class = UserQAProfileSerializer


class UserQAProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserQAProfile.objects.all()
    serializer_class = UserQAProfileSerializer
    lookup_field = 'pk'
