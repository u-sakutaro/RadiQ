from django import forms
from .models import Comment
 
 
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('target', 'date_posted', 'author', 'likes')
