from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Post
from ..serializers import PostSerializer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class IsSuperUserOrReadOnly(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in ["PUT", "PATCH", "POST", "DELETE"]:
            return request.user.is_superuser
        return True


class PostListCreateAPIView(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(type(request.data))
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def get_object(self, uuid):
        try:
            return Post.objects.get(uuid=uuid)
        except Post.DoesNotExist:
            return None

    def get(self, request, uuid, *args, **kwargs):
        post = self.get_object(uuid)
        if post is not None:
            serializer = PostSerializer(post)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, uuid, *args, **kwargs):
        post = self.get_object(uuid)
        if post is not None:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, uuid, *args, **kwargs):
        post = self.get_object(uuid)
        if post is not None:
            post.delete()
            return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Объект не найден"}, status=status.HTTP_404_NOT_FOUND)
