from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path("posts/", views.ListCreateView.as_view(), name="post-list-create"),
    path('posts/<uuid:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-delete'),
    path('questions/', views.QuestionListCreateView.as_view(), name="question-list-create"),
    path("qa/", views.UserQAProfileListCreateAPIView.as_view(), name="qa-list-create"),

]
