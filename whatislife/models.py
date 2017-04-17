from __future__ import unicode_literals

from django.db import models

import datetime
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    entry_title = models.CharField(max_length = 200)
    post_entry = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.entry_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_entry = models.CharField(max_length = 1000)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.comment_entry
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)