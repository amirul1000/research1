from django import forms
from accounts.models import UserProfile,ContactMemberMessage,Skill,SkillSubskill
from django.forms import ModelForm, Select

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationFrom(UserCreationForm):
    email      = forms.EmailField(required=True)
    first_name = forms.CharField(label = "First name")
    last_name  = forms.CharField(label = "Last name")

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

# CHOICES = (('a','A'),
#            ('b', 'B'),
#            ('c', 'C'),)

class UserForm(forms.ModelForm):  
    class Meta:
        model = User
        exclude = ['email',]

class UserProfileForm(forms.ModelForm):
    latitude   = forms.CharField(widget = forms.HiddenInput(), required = False)
    longitude  = forms.CharField(widget = forms.HiddenInput(), required = False)
    about_me  = forms.CharField(widget=forms.Textarea(attrs={'maxlength' : '500','style':"margin: 0px; width: 90%; height: 180px;"}),label = "About me", required = False)
    contact_details  = forms.CharField(widget=forms.Textarea(attrs={'maxlength' : '500','style':"margin: 0px; width: 90%; height: 180px;"}),label = "Contact details", required = False)
    class Meta:
        model = UserProfile
        exclude = ['user',]

class ContactMemberMessageForm(forms.ModelForm):
    class Meta:
       model  = ContactMemberMessage
       exclude = ['sender','receiver',]

class SkillSubskillForm(forms.ModelForm):
        #skill = forms.CharField(widget=forms.ModelChoiceField(attrs={'class' : '.myskillclass'}),label = "Skill")
        skill       = forms.ModelChoiceField(queryset=Skill.objects.all().order_by('name'), widget=Select(attrs={'class' : 'myskillclass'}))
        sub_skills  = forms.CharField(widget=forms.Textarea(attrs={'class' : 'mysubskillclass'}),label = "Sub skills")

        model = SkillSubskill
        exclude = ['profile',]
        