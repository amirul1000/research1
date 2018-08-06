from django.contrib import admin

# Register your models here.
from accounts.models import Research,Skill,Subskill,SkillSubskill,UserProfile,ContactMemberMessage
from machine.models import  Machine,Department

class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ('name', 'slug')

class ResearchAdmin(admin.ModelAdmin):
    model = Research
    list_display = ('name', 'slug')


class SubskillillInline(admin.StackedInline):
    model = Subskill
    extra = 1   

class SkillsAdmin(admin.ModelAdmin):
    model = Skill
    list_display = ('name', 'slug')

    inlines = [SubskillillInline]

class SkillSubskillInline(admin.StackedInline):
    model = SkillSubskill
    extra = 1      

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('user','get_full_name','department', 'country','research','machine')#,'get_skills','sub_skills')
    search_fields = ['user__username','department__name','research','machine']#,'skills__name','sub_skills']
    
    inlines = [SkillSubskillInline]
 

class ContactMemberMessageAdmin(admin.ModelAdmin):  
    model = ContactMemberMessage  
    list_display = ('subject','message','duration','sender','receiver')

admin.site.register(Research, ResearchAdmin)
admin.site.register(Skill, SkillsAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(ContactMemberMessage, ContactMemberMessageAdmin)