from __future__ import unicode_literals
from ..login_app.models import User

from django.db import models

# Create your models here.

class ReviewManager(models.Manager):
    def validate(self, postData):
        results = {'errors': []}

        if len(postData['author_name']) == 0:
            results['errors'].append("Please enter an author")

        if len(postData['comment']) == 0:
            results['errors'].append("Please enter a review, or return to homepage.")
        return results

    def recent_and_not(self):
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])

class Author(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    title = models.CharField(max_length=255)
    writer = models.ForeignKey(Author, related_name='authors')

class Review(models.Model):
    comment = models.TextField()
    rating = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name= 'posters')
    book = models.ForeignKey(Book, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ReviewManager()



  