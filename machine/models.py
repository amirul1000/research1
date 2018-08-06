from django.db import models
# Create your models here.

from django.contrib.auth.models import User
#from accounts.models import  Department

class Department(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Machine(models.Model):
    name_of_device            =    models.CharField(max_length=255,unique=True, blank=True, null=True)
    profile_picture           =    models.FileField(upload_to='assets/machine-profile/%Y/%m/%d',blank=True, null=True)  
    department                =    models.ForeignKey(Department)
    short_description         =    models.TextField(blank=True, null=True)  
    description               =    models.TextField(blank=True, null=True)
    #pdf_files                =    models.FileField(upload_to='documents/%Y/%m/%d',blank=True, null=True)    
    youtube_video             =    models.CharField(max_length=255, blank=True, null=True)
    web_links                 =    models.CharField(max_length=255, blank=True, null=True)
    working                   =    models.CharField(max_length=32, choices=( ('yes', 'yes'),('partial', 'partial'),('no', 'no')), blank=True)
    working_comments          =    models.TextField( blank=True, null=True)
    date_of_working           =    models.DateField( blank=True, null=True)
    mentor                    =    models.ManyToManyField(User, related_name="Mentor", blank=True) 
    booking_links             =    models.CharField(max_length=255, blank=True, null=True)
    editor                    =    models.ManyToManyField(User, blank=True) 
    subscriber                =    models.ManyToManyField(User, related_name="Subscriber", blank=True) 
    tag                       =    models.CharField(max_length=32, choices=( ('tag1', 'tag1'),('tag2', 'tag2'),('tag3', 'tag3'),('tag4', 'tag4'),('tag5', 'tag5')), blank=True)

    def __str__(self):
        return self.name_of_device
class UploadFiles(models.Model):
    page        =    models.ForeignKey(Machine)
    title       =    models.CharField(max_length=255, blank=True, null=True) 
    pdf_files   =    models.FileField(upload_to='documents/%Y/%m/%d',blank=True, null=True)            

class Faq(models.Model):
     page     =    models.ForeignKey(Machine)
     quistion = models.CharField(max_length=255, blank=True, null=True)
     answer   = models.CharField(max_length=255, blank=True, null=True)
     def __str__(self):
        return self.quistion         

class Message(models.Model):
    #machine      = models.ForeignKey(Machine)Question or Problem
    message_type = models.CharField(max_length=32, choices=( ('Question', 'Question'),('Problem', 'Problem')), blank=True)
    description  = models.TextField()  
    mentor       = models.ForeignKey(User,related_name="PageMentor+", blank=True, null=True) 
    sender       = models.ForeignKey(User,related_name="PageSender+", blank=True, null=True) 
    #def __str__(self):
    #    return self.sender.first_name+" "+ self.sender.last_name
