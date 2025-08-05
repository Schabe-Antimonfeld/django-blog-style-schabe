from django.contrib import admin

from .models import Topic, BlogPost

admin.site.register(Topic)
admin.site.register(BlogPost)
