from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from accounts.models import  Department
from machine.models import Machine,Faq,Message,UploadFiles



class FaqInline(admin.StackedInline):
    model = Faq
    extra = 1 

class UploadFilesInline(admin.StackedInline):
    model = UploadFiles
    extra = 1     
   
class MachineAdmin(admin.ModelAdmin):
    model = Machine
    list_display = ('name_of_device','department','description','youtube_video','web_links','working','working_comments')

    inlines = [UploadFilesInline,FaqInline]

class MessageAdmin(admin.ModelAdmin):
    model = Message
    #list_display = ('machine', 'description','mentor','sender')
    list_display = ('description','mentor','sender')
    
admin.site.register(Machine, MachineAdmin)   
admin.site.register(Message, MessageAdmin)   
