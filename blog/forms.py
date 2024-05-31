from django import forms
from django.contrib.auth import get_user_model

from blog.models import Comment, Post


class PostModelForms(forms.ModelForm):
    # title = forms.CharField()
    # content = forms.CharField(wiget=forms.TextInput())
    # author = forms.ChoiceField(queryset=get_user_model().objects.all())
    class Meta:
        model = Post
        fields = ('title', 'content', 'author')


class CommentModelForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'text', 'author' )
