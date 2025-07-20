from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=False)
    summary = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
