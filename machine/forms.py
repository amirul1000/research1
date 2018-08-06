from django import forms
from machine.models import Machine,UploadFiles,Faq,Message,UploadFiles

from django.contrib.auth.models import User

class MachineFrom(forms.ModelForm):    
    description      = forms.CharField(widget=forms.Textarea(attrs={'maxlength' : '1000','style':"margin: 0px; width: 90%; height: 220px;"}),label = "Description")
    youtube_video    = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':60}))
    web_links        = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':60}))
    working          = forms.Select()#widget=forms.Select(attrs={'onChange':'alert(1);'})
    working_comments = forms.CharField(required=False,label='')
    date_of_working  = forms.DateField(widget=forms.TextInput(attrs={'class' : 'datepicker'}),required=False,label='')
    class Meta:
        model = Machine
        fields = ('name_of_device','department','short_description','description','youtube_video','web_links','booking_links','working','working_comments','date_of_working','tag')

class UploadFilesFrom(forms.ModelForm):   
    class Meta:
        model = UploadFiles
        fields = ('title','pdf_files',)

class FaqFrom(forms.ModelForm):   
    class Meta:
        model = Faq
        fields = ('page','quistion','answer',)

class MessageForm(forms.ModelForm):   
    
    class Meta:
        model = Message
        fields = ('message_type','description',) 

    
                      
   