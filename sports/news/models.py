from django.db import models
from category.models import Category


class News(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    photo = models.ImageField()
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # author = models.ForeignKey()
