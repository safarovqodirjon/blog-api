from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView

app_name = "post"

urlpatterns = [
    path('list/', PostListCreateAPIView.as_view(), name='post-list'),
    path('detail/<uuid:uuid>/', PostDetailAPIView.as_view(), name='post-detail'),
]
