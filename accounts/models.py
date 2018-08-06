from django.db import models
from machine.models import  Machine,Department

# Create your models here.
__author__ = 'harri' # 2016-09-27

from django.contrib.auth.models import User
from accounts.country_codes import COUNTRY_CHOICES
from accounts.role_codes import ROLE_CHOICES


class Research(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(unique=True,max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    picture = models.FileField(upload_to='assets/pictures/%Y/%m/%d',blank=True, null=True)  
    picture_low_res = models.FileField(upload_to='assets/pictures/%Y/%m/%d',blank=True, null=True)  
    def __str__(self):
        return self.name

class Subskill(models.Model):
    skill         = models.ForeignKey(Skill, blank=True, null=True)
    sub_skills    = models.CharField(max_length=512, blank=True, null=True)
    def __str__(self):
        return self.skill.name        

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, primary_key=True)    
    country = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
    zip_code       = models.CharField(max_length=255, blank=True, null=True)  
    department = models.ForeignKey(Department, blank=True, null=True)
    role       = models.CharField(max_length=32, choices=ROLE_CHOICES, blank=True)
    research  =   models.TextField(blank=True, null=True)
    #machine  =  models.ManyToManyField(Machine, blank=True)
    machine  =  models.TextField(blank=True, null=True)
    about_me  = models.TextField(blank=True, null=True)
    contact_details = models.TextField(blank=True, null=True)
    latitude       = models.CharField(max_length=512, blank=True, null=True)  
    longitude       = models.CharField(max_length=512, blank=True, null=True)  
    def get_full_name(self):
           return self.user.first_name+" "+self.user.last_name
    #def get_research(self):
    #    return ",".join([str(p) for p in self.research.all()])
    def get_skills(self):
        skillsubskill = self.skillsubskill_set.all()
        if skillsubskill.count()>0:
                return ",".join( [x.skill.name for x in skillsubskill])
    def get_sub_skills(self):
        skillsubskill = self.skillsubskill_set.all()
        if skillsubskill.count()>0:
                return ",".join( [x.sub_skills for x in skillsubskill])            

    def __str__(self):
        return self.user.username

User.profile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])

class SkillSubskill(models.Model):
    user_profile  = models.ForeignKey(UserProfile)
    skill         = models.ForeignKey(Skill, blank=True, null=True)
    sub_skills    = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.skill.name

class ContactMemberMessage(models.Model):
    subject        = models.CharField(max_length=255, blank=True, null=True)
    message        = models.TextField()  
    duration       = models.CharField(max_length=255, blank=True, null=True)  
    sender         = models.ForeignKey(User,related_name="Sender", blank=True, null=True) 
    receiver       = models.ForeignKey(User,related_name="Receiver", blank=True, null=True)    