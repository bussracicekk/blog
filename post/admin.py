from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'DateOfPublished']
    list_display_links = ['title', 'DateOfPublished']
    list_filter = ['DateOfPublished']
    search_fields = ['title', 'content']
    # list_editable = ['title']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
