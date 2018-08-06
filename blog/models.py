from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Content(models.Model):
    content_text  =  models.TextField()
    poster        =  models.ForeignKey(User,related_name="Poster", blank=True, null=True) 
    def __str__(self):
        return self.content_text    

class Comment(models.Model):
    content         = models.ForeignKey(Content)
    comment_text    = models.TextField()
    commenter       = models.ForeignKey(User,related_name="Commenter", blank=True, null=True) 
    def __str__(self):
        return self.comment_text                      
