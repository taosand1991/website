from django.contrib import admin
from .models import Post, Comment, Category
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'status')


admin.site.register(Comment)
admin.site.register(Category)