from django.contrib import admin
from ..models import Article
from ..models import Tag
from ..models import Comment
from ..models import Media
# Register your models here.

class TagsInline(admin.TabularInline):
    model = Article.tags.through


class CommentsInline(admin.TabularInline):
    model = Comment


class MediumInline(admin.TabularInline):
    model = Article.medium.through


class ArticleAdmin(admin.ModelAdmin):
    fields = ('lang', 'name', 'title', 'content_type', 'content', 'description', )
    list_filter = ('lang',)
    search_fields = ('name', 'title')
    list_display = ('name', 'title', 'lang', 'created_time', 'modified_time')
    inlines = (MediumInline, TagsInline, CommentsInline)


admin.site.register(Article, ArticleAdmin)