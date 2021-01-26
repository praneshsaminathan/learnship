from django.contrib import admin
from .models import Article, Comment
# Register your models here.


admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'slug')

    fields = ('title', 'content', 'slug')

    def title_case_name(self, obj):
        return obj.title.title()

