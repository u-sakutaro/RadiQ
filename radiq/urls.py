from django.urls import path
from . import views

app_name = 'radiq'

urlpatterns = [
    path('', views.PostListView.as_view(), name='radiq-home'),
    path('post/new', views.PostCreateView.as_view(), name='post-create'),
    path('not', views.notCreatedView, name='not-created'),
]


