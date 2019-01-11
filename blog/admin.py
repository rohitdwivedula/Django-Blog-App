from django.contrib import admin
from .models import BlogPost, Feedback

admin.site.register(BlogPost)
admin.site.register(Feedback)