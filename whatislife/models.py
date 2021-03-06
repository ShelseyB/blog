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
    
    
class CommentManager(models.Manager):
    def create_comment(self, post_pk, comment_entry, comment_author):
    #     #book = cls(title=title)
        comment = self.create(post_pk=post_pk, comment_entry=comment_entry, comment_author=comment_author)
        return comment    

class Comment(models.Model):
    post_pk = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_entry = models.CharField(max_length = 1000)
    #pub_date = models.DateTimeField('date published')
    comment_author = models.CharField(max_length = 200)
    objects = CommentManager()
    def __str__(self):
         return self.comment_entry
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # def create_comment(self, cls, post, comment_entry, pub_date, comment_author):
    #     #book = cls(title=title)
    #     comment = cls (post=post, comment_entry=comment_entry, pub_date=pub_date, comment_author=comment_author)
    #     return comment
    

        
# class BookManager(models.Manager):
#     def create_book(self, title):
#         book = self.create(title=title)
#         # do something with the book
#         return book

# class Book(models.Model):
#     title = models.CharField(max_length=100)

#     objects = BookManager()

# book = Book.objects.create_book("Pride and Prejudice")
        
#         class Book(models.Model):
#     title = models.CharField(max_length=100)

#     @classmethod
#     def create(cls, title):
#         book = cls(title=title)
#         # do something with the book
#         return book

# book = Book.create("Pride and Prejudice")

        
        

        
        