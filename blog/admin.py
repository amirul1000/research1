from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from blog.models import Content,Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1  
    #template = "admin/machine/page/edit_inline/stacked.html"  

class ContentAdmin(admin.ModelAdmin):
    model = Content
    list_display = ('content_text','poster')
    inlines = [CommentInline]

admin.site.register(Content, ContentAdmin)   