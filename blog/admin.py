from django.contrib import admin
from blog.models import Article, Tag

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
