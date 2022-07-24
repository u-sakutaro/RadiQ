from django.urls import path
from . import views

app_name = 'radiq'

urlpatterns = [
    path('', views.PostListView.as_view(), name='radiq-home'),
    path('post/new', views.PostCreateView.as_view(), name='post-create'),
    path('not', views.notCreatedView, name='not-created'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='post-comment'),
]

