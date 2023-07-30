from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Post
from ..serializers import PostSerializer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.authentication import TokenAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from rest_framework import exceptions


class ListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.prefetch_related('questions')
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
