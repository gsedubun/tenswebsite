from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Post
from .resources import PostResource

# Register your models here.



admin.site.register(Post)

class PostAdmin(ImportExportActionModelAdmin):
    resource_class = PostResource