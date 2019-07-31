from django.contrib import admin

# Register your models here.
from .models import Thread, Post

admin.site.register(Thread)
admin.site.register(Post)
