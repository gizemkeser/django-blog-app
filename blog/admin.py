from django.contrib import admin

from blog.models import Post, Author, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'body', 'author', 'display_tag']
    readonly_fields = ('slug',)


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
