from django.contrib import admin

from .models import blog_text, user_password

admin.site.register(user_password)
admin.site.register(blog_text)
