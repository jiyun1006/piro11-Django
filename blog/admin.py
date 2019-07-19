from django.contrib import admin
from .models import Post




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at','updated_at'
    ]

#admin.site.register(Post,PostAdmin) 얘하고 데코레이터하고 기능 똑같음.







# class ResourceAdmin(admin,ModelAdmin):
#     list_display = ('id', 'name')
#
# admin.site.register(Resource,ResourceAdmin)