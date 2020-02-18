from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    stars = models.DecimalField(max_digits=3, decimal_places=2,default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def number_of_ratings(self):
        ratings = Post.objects.filter(book_title=self)
        return len(ratings)
    
    def avg_rating(self):
        sum = 0
        ratings = Post.objects.filter(book_title=self)
        for post in ratings:
            sum += post.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0
    
    def __str__(self):
        return self.book_title
