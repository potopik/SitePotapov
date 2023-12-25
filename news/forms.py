from django import forms

from news.models import Comment, Post


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('tags', 'title', 'slug', 'author', 'body', 'image', 'publish', 'status')
