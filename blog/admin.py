from django.contrib import admin
from .models import Post

admin.site.register(Post)


# class ResourceAdmin(admin,ModelAdmin):
#     list_display = ('id', 'name')
#
# admin.site.register(Resource,ResourceAdmin)