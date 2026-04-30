from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=100, default="Game News")
    image = models.ImageField(upload_to='posts/')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="Admin")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game_name = models.CharField(max_length=200)
    edition = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Completed')

    def __str__(self):
        return f"Order {self.id} - {self.game_name} ({self.user})"
