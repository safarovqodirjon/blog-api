from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView
from .views.user_qa_profile import UserQAProfileListCreateAPIView, UserQAProfileDetailAPIView

app_name = "post"

urlpatterns = [
    path('list/', PostListCreateAPIView.as_view(), name='post-list'),
    path('detail/<uuid:uuid>/', PostDetailAPIView.as_view(), name='post-detail'),

    path('profiles/', UserQAProfileListCreateAPIView.as_view(), name='user-profile-list'),
    path('profiles/<int:pk>/', UserQAProfileDetailAPIView.as_view(), name='user-profile-detail'),
]
