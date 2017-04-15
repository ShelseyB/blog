from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    post_entry = models.CharField(max_length=3000)
    pub_date = models.DateTimeField('date published')
    
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_entry = models.CharField(max_length = 1000)
    pub_date = models.DateTimeField('date published')