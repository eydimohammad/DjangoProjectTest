from django.contrib import admin
from .models import Article, Category


# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    title = "title"
    content = "summary"
    published_date = "published_at"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass