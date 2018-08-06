from accounts.models import Skill,Subskill,UserProfile
from machine.models import Machine
import re

""""
   save new sub_skills to Skill Model
"""
def  save_skill(skill,sub_skills):
    sub_skills_list = sub_skills.split(',')
    obj_skill = Skill.objects.get(pk=skill)
    sub_skills = obj_skill.subskill_set.all() 
    
    ####### get previous subskill
    sub_skills_list2 = []
    for each in sub_skills:
       sub_skills_list2.append(each.sub_skills)
       
    ##########save new data
    for each in sub_skills_list:
    	if each not in sub_skills_list2:
    		obj = Subskill(skill=obj_skill)
    		obj.sub_skills = each
    		obj.save()

""""
   generate predefined  key word 
   from UserProfile Model
"""
def member_serack_keyword():
    str1   = ""
    list2  = [] 
    list3  = []
    user_profile = UserProfile.objects.all()
    
    all_data2 = [e.country for e in user_profile]
    all_data3 = [e.department for e in user_profile]
    all_data4 = [e.research for e in user_profile]
    
    
    for each_user in user_profile:
        user_profile_each =  UserProfile.objects.get(pk=each_user.pk)
        skillsubskill = user_profile_each.skillsubskill_set.all()
        if skillsubskill.count()>0:
                list1 = [x.skill.name for x in skillsubskill]
                list2.extend(list1)                
                list1 = [x.sub_skills for x in skillsubskill]
                for each in list1:
                    if each:
                        list3 = [str(x) for x in each.split(',')]  
                        list2.extend(list3)
             
    for e in all_data4:
        try:
            list1 = [str(x) for x in re.split(',',e) if x!='']
            list2.extend(list1) 
        except:
          pass


    for e in all_data2:
        try:
            list1 = [str(x) for x in re.split(',',e) if x!='']
            list2.extend(list1) 
        except:
          pass

    for e in all_data3:
        try:
           list1 = [e.name]
           list2.extend(list1)  
        except:
          pass

    for x in user_profile:
        try:
            #username = x.user.username
            email    = x.user.email
            first_name    = x.user.first_name
            last_name    = x.user.last_name
            if first_name:
               if last_name:
                  if email:    
                    list1 = [str(email),str(first_name),str(last_name)]
                    list2.extend(list1)
        except:
            False  

    machines = Machine.objects.all()
    for each in machines:
        list1 = [str(each.name_of_device)]
        list2.extend(list1)
    
    try:        
      list2 = sorted(list2) 
    except:
            False  
    try:
      list2 = list(set(list2))  
    except:
            False  


    return list2