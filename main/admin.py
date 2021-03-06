from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', )
	readonly_fields = ('created_at', 'updated_at', )
	search_fields = ['title', 'subtitle', 'content', 'created_at', 'updated_at', ]

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'post', 'author', 'message', )
	readonly_fields = ('created_at', 'updated_at', )
	search_fields = ['post', 'author', 'message', 'created_at', 'updated_at', ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)