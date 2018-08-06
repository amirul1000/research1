from django.shortcuts import  get_object_or_404, render
# Create your views here.
from django.http import HttpResponseRedirect
from django.http.request import QueryDict, MultiValueDict

import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from machine.forms import MessageForm,MachineFrom,UploadFilesFrom,FaqFrom
from django.forms import inlineformset_factory

from machine.models import Machine,Faq,Message,UploadFiles
from accounts.models import UserProfile
from django.core.mail import send_mail


from django.contrib import auth
from django.contrib.auth.models import User

from django.template import *



def devices(request):
    ##################selectize###############
    '''    str1   = ""
    list2  = [] 
    machine = Machine.objects.all()

    all_data1 = [e.name_of_device for e in machine]
    all_data2 = [e.department.name for e in machine]
    
    for e in all_data1:
        try:
            list1 = [x for x in re.split(',',e) if x!='']
            list2.extend(list1)
        except:
          pass 
    for e in all_data2:
        try:
            list1 = [x for x in re.split(',',e) if x!='']
            list2.extend(list1) 
        except:
          pass
    list2 = sorted(list2) 
    list2 = list(set(list2))
    ''' 
    ############################################# 

    if request.POST.get('new_machine') == 'add_new': 
            #faqformset = inlineformset_factory(Machine,Faq,fields=('quistion','answer',),extra=1)
            if request.method == 'POST':
                #machine_form = MachineFrom(request.POST)
                #print(machine_form)
                #if machine_form.is_valid():    
                    #print(".......Helloooo")                 
                    #machine = machine_form.save(commit=False)
                try:
                    machine         = Machine(name_of_device=request.POST.get('name_of_device'),department_id=request.POST.get('department'))
                    machine.working = 'yes'
                    machine.save()
                    #faqformset = faqformset(request.POST,instance=machine)
                    #if faqformset.is_valid():
                    #     faqformset.save() 
                    machine.editor.add(User.objects.get(pk=request.user.pk))
                except:
                    pass


    #search by query
    q            = ""
    q1           = ""
    query        = ""
    if request.GET.get('q'):
        q = request.GET.get('q').strip()
        q1  = q 
        arr_q = q.split(',')
        k=1
        for q in  arr_q:
            query1  = Q(name_of_device__contains=q) |  Q(department__name__contains=q)
            if k==1: 
              query   =  query1
              k=k+1             
            else:
              query   =  query & query1
        machine_list = Machine.objects.all().filter( query ).distinct().order_by('-id')
    else:      
        machine_list = Machine.objects.all().order_by('-id')

    paginator = Paginator(machine_list, 25) # Show 25 contacts per Machine
    page = request.GET.get('page')
    try:
        machines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        machines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        machines = paginator.page(paginator.num_pages)

    form  = MachineFrom()
    #faqformset = inlineformset_factory(Machine,Faq,fields=('quistion','answer',),extra=1)    
    
    return render(request, 'devices.html', { 'machines':machines,'page_form':form,'q':q1})

#@login_required
def page(request,name_of_device):
    page    = Machine.objects.get(name_of_device__contains=name_of_device)
    return render(request, 'page_view.html', { 'page':page})
#edit Machine by login user/editor
@login_required
def page_edit(request,machine_id):
    message_str = ""
    machine = Machine.objects.get(pk=machine_id)    
    qr_code = machine.name_of_device
    form  = MachineFrom(instance=machine)
    faqformset    = inlineformset_factory(Machine,Faq,fields=('quistion','answer',),extra=1,form=FaqFrom)
    uploadformset = inlineformset_factory(Machine,UploadFiles,fields=('title','pdf_files',),extra=1,form=UploadFilesFrom)
    if request.method == 'POST':
        machine_form = MachineFrom(request.POST, request.FILES,instance=Machine.objects.get(pk=machine_id))
        if machine_form.is_valid():
            machine = machine_form.save(commit=False)
            machine.save()  

            formset = faqformset(request.POST,instance=machine)
            if formset.is_valid():
               formset.save()

            formset2 = uploadformset(request.POST,request.FILES,instance=machine)
            if formset2.is_valid():
               #pdf_files =  cleaned_data['pdf_files']
               formset2.save()
            #delete all
            #faq = Faq.objects.all()
            #faq.page = machine
            #faq.delete()

            #quistion = request.POST.getlist("quistion[]")
            #answer = request.POST.getlist("answer[]")

            #for key,val in enumerate(quistion):              
            #    faq = Faq()
            #    faq.page = machine
            #    faq.quistion = val
            #    faq.answer   = answer[key]
            #    faq.save() 
                 #dispaly new data
            machine = Machine.objects.get(pk=machine_id) 
            form    = MachineFrom(instance=machine)           

            message_str = "Machine has been updated successfully!!!"
            #edited by   
            machine.editor.add(User.objects.get(pk=request.user.pk))
            
            #send email
            if machine.working == 'partial' or machine.working == 'no':
                sender_email = request.user.email
                description  = machine.working_comments
                for each in  machine.subscriber.all():
                    subscriber_email = each.email
                    try:
                        send_mail(
                                'Working status comments on '+machine.name_of_device,
                                 description,
                                 sender_email ,
                                 [subscriber_email],
                                 fail_silently=Ture,
                                 )
                    except:
                           pass    
        return redirect('page',machine.name_of_device)             
    else:  
        machine = Machine.objects.get(pk=machine_id) 
        form  = MachineFrom(instance=machine)                    
        faqformset = faqformset(instance=machine)
        uploadformset = uploadformset(instance=machine)
        page    = Machine.objects.get(name_of_device__contains=machine.name_of_device)
     
    return render(request, 'page_edit.html', { 'page_form':form,'faqformset':faqformset,'uploadformset':uploadformset,'page':page,'qr_code':qr_code,'message':message_str})
    
#send email to all  mentor
@login_required
def send_message(request,machine_id):
    message_str = ""
    if request.method == 'POST':
        machine = Machine.objects.get(pk=machine_id) 
        machine_pk = machine.pk
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            #message.machine = Machine.objects.get(pk=machine_pk)
            message.sender  = User.objects.get(pk=request.user.pk)
            message.save()

            message_str = "Message has been sent successfully!!!"
            #send email
            sender_email = request.user.email
            message_type  = request.POST.get('message_type')
            description  = request.POST.get('description')
            for each in  machine.mentor.all():
                mentor_email = each.email
                try:
                    send_mail(
                            message_type+' '+machine.name_of_device,
                             description,
                             sender_email ,
                             [mentor_email],
                             fail_silently=Ture,
                             )
                except:
                       pass    

    machine = Machine.objects.get(pk=machine_id) 
    qr_code = machine.name_of_device
    form  = MessageForm()
    return render(request, 'page_message.html', { 'message_form':form,'qr_code':qr_code,'message':message_str})
#downlaod pdf
@login_required    
def download(request,file_id): 
    from django.http import HttpResponse
    from os.path import basename
    uploadfiles = UploadFiles.objects.get(pk=file_id)      
    pdf_files  = str(uploadfiles.pdf_files)
    file_name = basename(pdf_files)

    with open(pdf_files, 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename='+file_name
        return response
    pdf.closed
        
#be mentor    
@login_required    
def be_mentor(request,machine_id):     
    machine = Machine.objects.get(pk=machine_id) 
    if request.user in machine.mentor.all():
       machine.mentor.remove(User.objects.get(pk=request.user.pk)) 
    else:    
       machine.mentor.add(User.objects.get(pk=request.user.pk))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#subscribe
@login_required    
def subscribe(request,machine_id):     
    machine = Machine.objects.get(pk=machine_id) 
    if request.user in machine.subscriber.all():
       machine.subscriber.remove(User.objects.get(pk=request.user.pk)) 
    else:    
       machine.subscriber.add(User.objects.get(pk=request.user.pk))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))