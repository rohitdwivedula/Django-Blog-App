from django.contrib import admin
from .models import BlogPost, Feedback

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'text', 'author', 'published_date')

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'text', 'message_id', 'published_time');

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Feedback, FeedbackAdmin)
