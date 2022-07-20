from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect

from .models import Post


# Postの内容を表示する
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    # どのHTMLを表示するか↓
    template_name='radiq/index.html'
    # 表示順序↓
    ordering = ['-date_posted']
    # 表示件数↓
    pagenate_by = 5     

# 新規投稿する
class PostCreateView(CreateView):
    model = Post
    # どのfieldsを使うか(models.pyで定義したプロパティの中で)
    fields = ['content']
    template_name = 'radiq/post_create.html'
    success_url = '/'



# 未作成URLをreturnする
def notCreatedView(request):
    return render(request, 'radiq/not_created.html')