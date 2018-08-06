from django.shortcuts import render
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from accounts.forms import UserForm,UserProfileForm, RegistrationFrom , ContactMemberMessageForm,SkillSubskillForm
from accounts.models import Skill,Subskill,Research,UserProfile,SkillSubskill,ContactMemberMessage
from django.contrib import auth
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory

import json
from collections import Counter
from accounts.accounts_lib import *
from accounts.templatetags import color_text
from machine.models import  Machine,Department

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

    return render(request, 'login.html')

@login_required
def logout(request):

    auth.logout(request)
    return redirect('/')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('/accounts/profile')
            return redirect('/accounts/welcome')

    else:
        form = RegistrationFrom()

    return render(request, 'register.html', { 'register_form':form })
@login_required

def welcome_view(request):
 ##################selectize###############
   
    str1   = ""
    list2  = [] 
    
    sub_skills = Subskill.objects.all()
    for e in sub_skills:
        try:
            list1 = [e.sub_skills]
            list2.extend(list1)
        except:
          pass     
    list2 = sorted(list2) 
    list2 = list(set(list2)) 
    
    ############################################# 
    extra = 1
    try:
        if request.user:
            skill = SkillSubskill.objects.all().filter(user_profile=UserProfile.objects.get(user=request.user))
            if skill.count()>0:
                extra = 1#5-skill.count()
            else:
                extra = 2
    except:
       pass        
    SkillSubskillSet = inlineformset_factory(UserProfile,SkillSubskill,fields=('skill','sub_skills',),extra=extra,form=SkillSubskillForm)
    '''
    if request.POST.get('new_skill') == 'add_new':
        skill = request.POST.get("skillsubskill_set-0-skill")
        sub_skills = request.POST.get("skillsubskill_set-0-sub_skills")

        user = request.user
        profile = user.profile    
        skill_obj            = SkillSubskill(user_profile=profile)
        skill_obj.skill      = Skill.objects.get(pk=skill)
        skill_obj.sub_skills = sub_skills
        skill_obj.save()
        #new subskill insert in Model
        save_skill(skill,sub_skills)
        return redirect('/accounts/profile/')
    el
    '''
    if  request.method == "POST":
        form = UserProfileForm(request.POST,
                               instance=request.user.profile)
        skillformset = SkillSubskillSet(request.POST)

        if form.is_valid():
            profile   = form.save(commit=False)
            skillformset = SkillSubskillSet(request.POST,instance=profile)

            user = request.user
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.save()
            ##############save form set############
            if skillformset.is_valid():
                    profile.research = form.cleaned_data['research']
                    profile.machine  = form.cleaned_data['machine']
                    profile.save()
                    skillformset.save() 

                    #new subskill insert in Model
                    for form in skillformset:
                        try:
                            skill = form.cleaned_data['skill']
                            sub_skills = form.cleaned_data['sub_skills']          
                            if skill:
                                skill = Skill.objects.get(name__exact=skill)
                                skill = skill.pk                                              
                                save_skill(skill,sub_skills)     
                        except:
                            pass
            return redirect('/accounts/welcome/')
    #else:    
    
    user = request.user
    profile = user.profile    
    form = UserProfileForm(instance=profile)
    user_form = UserForm(instance=user)
    skillformset = SkillSubskillSet(instance=profile)
    
    skill_empty_form = SkillSubskillSet()
    skill_empty_form.extra=1

    machine_list  = Machine.objects.all().order_by('name_of_device')
    research_list = Research.objects.all().order_by('name')  
    
    return render(request, 'welcome.html', { 'profile_form':form,'skillformset':skillformset,
                                             'user_form':user_form,'skill_empty_form':skill_empty_form,
                                             'machine_list':machine_list,'research_list':research_list,
                                             'sub_skills':list2 })

@login_required
def user_profile(request):
    ##################selectize###############
   
    str1   = ""
    list2  = [] 
    
    sub_skills = Subskill.objects.all()
    for e in sub_skills:
        try:
            list1 = [e.sub_skills]
            list2.extend(list1)
        except:
          pass     
    list2 = sorted(list2) 
    list2 = list(set(list2)) 
    
    ############################################# 
    extra = 1
    try:
        if request.user:
            skill = SkillSubskill.objects.all().filter(user_profile=UserProfile.objects.get(user=request.user))
            if skill.count()>0:
                extra = 1#5-skill.count()
            else:
                extra = 2
    except:
       pass        
    SkillSubskillSet = inlineformset_factory(UserProfile,SkillSubskill,fields=('skill','sub_skills',),extra=extra,form=SkillSubskillForm)
    '''
    if request.POST.get('new_skill') == 'add_new':
        skill = request.POST.get("skillsubskill_set-0-skill")
        sub_skills = request.POST.get("skillsubskill_set-0-sub_skills")

        user = request.user
        profile = user.profile    
        skill_obj            = SkillSubskill(user_profile=profile)
        skill_obj.skill      = Skill.objects.get(pk=skill)
        skill_obj.sub_skills = sub_skills
        skill_obj.save()
        #new subskill insert in Model
        save_skill(skill,sub_skills)
        return redirect('/accounts/profile/')
    el
    '''
    if  request.method == "POST":
        form = UserProfileForm(request.POST,
                               instance=request.user.profile)
        skillformset = SkillSubskillSet(request.POST)

        if form.is_valid():
            profile   = form.save(commit=False)
            skillformset = SkillSubskillSet(request.POST,instance=profile)

            user = request.user
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.save()
            ##############save form set############
            if skillformset.is_valid():
                    profile.research = form.cleaned_data['research']
                    profile.machine  = form.cleaned_data['machine']
                    profile.save()
                    skillformset.save() 

                    #new subskill insert in Model
                    for form in skillformset:
                        try:
                            skill = form.cleaned_data['skill']
                            sub_skills = form.cleaned_data['sub_skills']          
                            if skill:
                                skill = Skill.objects.get(name__exact=skill)
                                skill = skill.pk                                              
                                save_skill(skill,sub_skills)     
                        except:
                            pass
            return redirect('/accounts/sciport/')
    #else:    
    
    user = request.user
    profile = user.profile    
    form = UserProfileForm(instance=profile)
    user_form = UserForm(instance=user)
    skillformset = SkillSubskillSet(instance=profile)
    

    skill_empty_form = SkillSubskillSet()
    skill_empty_form.extra=1

    machine_list  = Machine.objects.all().order_by('name_of_device')
    research_list = Research.objects.all().order_by('name')  
    
    return render(request, 'profile.html', { 'profile_form':form,'skillformset':skillformset,
                                             'user_form':user_form,'skill_empty_form':skill_empty_form,
                                             'machine_list':machine_list,'research_list':research_list,
                                             'sub_skills':list2 })

@property
def correctString(self):
    return str(self.replace(',',' '))
    
def members_directory(request):
     ##################selectize###############
    list2 = member_serack_keyword()
    ############################################# 

    #all User Profile
    members_list = ""

    #search by query
    q            = ""
    q1           = ""
    query        = ""
    if request.GET.get('q'):
        q = request.GET.get('q').strip()
        q1  = q 
        arr_q = q.split(',')        
        k=1
        for q2 in  arr_q:
            q2 = str(q2)
            query1  = Q(user__first_name__contains=q2) |  Q(user__last_name__contains=q2) | Q(user__username__contains=q2) |  Q(user__email__contains=q2) |   Q(department__name__contains=q2) | Q(country__contains=q2) | Q(research__contains=q2) | Q(machine__contains=q2)  | Q(skillsubskill__skill__name__contains=q2) | Q(skillsubskill__sub_skills__contains=q2) 
            if k==1: 
              members_list = UserProfile.objects.filter(query1)   
              query   =  query1
              k=k+1             
            else:
              members_list = members_list.filter(query1)     
              query   =  query & ( query1 )    
        members_list = members_list.distinct()                
        #members_list = UserProfile.objects.filter( Q(skillsubskill__skill__name__contains='Apoptosis') & Q(skillsubskill__sub_skills__contains='Cell Culture') )#.distinct()
    else:
        members_list = UserProfile.objects.all()      
    
    paginator = Paginator(members_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        members = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        members = paginator.page(paginator.num_pages)
    
    for each in members:
        list3 = []
        str1  = ""
        if each.get_sub_skills():
            list1 = each.get_sub_skills().split(',') 
            for e in list1:
                if e==q:
                    list3.extend([e+'&nbsp;'])
                else:
                    list3.extend(['<span style="padding: 5px; margin-bottom: 10px; border: 1px solid #a7a7a7; display: inline-block; border-radius: 10px;"> '+e+' </span>&nbsp;'])# for  arg  in list1]
           
            str1 = ''.join(str(e) for e in list3)
        each.get_sub_skills = str1

    
    return render(request, 'members.html', { 'members':members,'q':q1,'seelctize':list2 })
    
def members_network(request):
    list2  = [] 
    user_profile = UserProfile.objects.all()
    b = []
   
    for i in range(len(user_profile)):
        sub_str = user_profile[i].get_sub_skills()
        if sub_str:
            list1 = [x for x in re.split(',',sub_str) if x!='']
            b.extend(list1)
    n =' '.join(str(r) for r in  b)
    freqs = Counter(n.split())

   
    skill_counts = dict(freqs)
   
    
    d = {"name":"flare","children":[{'name':key,'size':value, 'mcperpatient':value,'displayname':key} for key,value in skill_counts.items()]}

    skill_countsJson = json.dumps(d) 
    
    '''  MAP '''
    from accounts.world import world
    members = UserProfile.objects.all()
    k=0
    for each in members:
        k=k+1
        name     = each.user.first_name+" "+each.user.last_name
        role     = each.role
        department = each.department
        about_me  = each.about_me
        contact_details = each.contact_details
        latitude = each.latitude
        longitude = each.longitude

        if about_me :
          if contact_details :
            if latitude : 
                if longitude :
                    each_dict =  { 
                                  "id":k,
                                  "title": name,
                                  "about": about_me,
                                  "description": contact_details,
                                  "pin": "circular pin-md pin-label",
                                  "label": k,
                                  "fill": "#f23543",
                                  "lat": latitude,
                                  "lng": longitude}
                    
                    world['levels'][0]['locations'].append(each_dict)   

    try:    
        return render(request, 'network.html', { 'members':list2, 'skill_json': skill_countsJson,'world':world})
    except:
         return render(request, 'network.html')
            

def contact_member_message(request,receiver_id):
    message_str = ""
    if request.method == 'POST':
        message             = ContactMemberMessage()
        message.sender      = User.objects.get(pk=request.user.pk)
        message.receiver    = User.objects.get(pk=receiver_id)
        message.duration    = request.POST.get('duration')
        message.message     = request.POST.get('message')
        message.subject     = request.POST.get('subject')

        message_form = ContactMemberMessageForm(instance=message)
        #if message_form.is_valid():
        message_form = message_form.save(commit=False)
        #message.machine = Machine.objects.get(pk=machine_pk)
        message_form.save()

        message_str = "Message has been sent successfully!!!"
        #send email
        sender_email = request.user.email
        receiver_email = message.receiver.email
        message =  request.POST.get('message')+' Duration:'+message.duration
        print(message)
        try:
            send_mail(
                     request.POST.get('subject'),
                     message,
                     sender_email ,
                     [receiver_email],
                     fail_silently=Ture,
                     )
        except:
               pass  

    user_profile = UserProfile.objects.get(user=User.objects.get(pk=receiver_id))
    form      = ContactMemberMessageForm()    

    from django.conf import settings
    doc_root  = settings.STATIC_ROOT
    #print(doc_root)
    return render(request, 'message.html', { 'message_form':form,'user_profile':user_profile,'receiver_id':receiver_id,'message':message_str,'doc_root':doc_root})

def json_data(request):  
    data = {'data':[{'key1':'val1'}, {'key2':'val2'}]}
    
    return HttpResponse(data)

def map_view(request):
    '''
    from accounts.world import world
    members = UserProfile.objects.all()
    print(members)
    k=0
    for each in members:
        k=k+1
        name     = each.user.first_name+" "+each.user.last_name
        role     = each.role
        department = each.department
        about_me  = each.about_me
        contact_details = each.contact_details
        latitude = each.latitude
        longitude = each.longitude

        if about_me :
          if contact_details :
            if latitude : 
                if longitude :
                    each_dict =  { 
                                  "id":k,
                                  "title": name,
                                  "about": about_me,
                                  "description": contact_details,
                                  "pin": "circular pin-md pin-label",
                                  "label": k,
                                  "fill": "#f23543",
                                  "lat": latitude,
                                  "lng": longitude}
                    
                    world['levels'][0]['locations'].append(each_dict)  
    ''' 
    return render(request, 'members_map.html', {'world':world })

    ##########################sciport############################
    #############################################################
def sciport_view(request):
    skill = Skill.objects.all()
    return render(request, 'sciport.html', {'skill':skill})

def sciport_subskill_view(request,sciport_name):
    skill = Skill.objects.get(name=sciport_name)
    return render(request, 'sciport_subskill.html', {'skill':skill})


def subskils(request,skill_id):
    data = []
    subskill = Subskill.objects.all().filter(skill__id__exact=skill_id)
    for each in subskill:
        sub = { 'id':each.id,
                'name':each.sub_skills,
                'url':each.sub_skills
                }
        data.append(sub)        
    import json
    j = json.dumps(data)
    return HttpResponse(j)

def search_text(request):
     ##################selectize###############
    list2 = member_serack_keyword()
    #############################################     
    import json
    j = json.dumps(list2)
    return HttpResponse(j)

