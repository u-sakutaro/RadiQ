from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic


from .models import Post, Comment
from .comment import CommentCreateForm


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
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # どのfieldsを使うか(models.pyで定義したプロパティの中で)
    fields = ['content']
    template_name = 'radiq/post_create.html'
    success_url = '/'
    # modelsからauthorの情報をリクエストしてPostCreateView内に返すメソッド
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


# 詳細を見る
class PostDetailView(DetailView):
    model = Post


# 投稿をUpdateする
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # どのfieldsを使うか(models.pyで定義したプロパティの中で)
    fields = ['content']
    template_name = 'radiq/post_update.html'
    success_url = '/'
    # modelsからauthorの情報をリクエストしてPostCreateView内に返すメソッド
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)
    # ログイン者とAuthorが一致しているか確認メソッド
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


# 投稿を削除する
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # どのfieldsを使うか(models.pyで定義したプロパティの中で)
    template_name = 'radiq/post_confirm_delete.html'
    success_url = '/'
    # ログイン者とAuthorが一致しているか確認メソッド
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


# 返信投稿のview
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'radiq/post_comment.html'
    form_class = CommentCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post   
        comment.save()
        return redirect('radiq:post-detail', pk=post_pk)


# 未作成URLをreturnする
def notCreatedView(request):
    return render(request, 'radiq/not_created.html')