from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ('title','slug','created_on','updated_on','status')
  list_filter = ('status', 'updated_on', 'created_on', "body",)
  search_fields = ('body','title', )
  prepopulated_fields = {'slug': ('title', )}


admin.site.register(Post, PostAdmin)
