from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path("posts/", views.ListCreateView.as_view(), name="post-list-create"),
    path('posts/<uuid:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-delete'),

]
