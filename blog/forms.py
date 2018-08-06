from django import forms
from blog.models import Content,Comment

from django.contrib.auth.models import User

class ContentFrom(forms.ModelForm): 
    class Meta:
        model = Content
        fields = ('content_text',)

class CommentFrom(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ('comment_text',)        