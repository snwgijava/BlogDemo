from django.contrib import admin
from .models import Post,Category,Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    #字段显示
    list_display = ['title','created_time','modified_time','category','author']
    #搜索
    search_fields = ['title']
    #筛选
    list_filter = ['created_time','tags','category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
