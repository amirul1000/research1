from django.conf.urls import url
from machine.views import devices,page_edit,page,send_message,download,be_mentor,subscribe

urlpatterns = [   
     url(r'^devices/', devices, name='devices'),
     url(r'^page/(.*?)/', page, name='page'),
     url(r'^page_edit/(?P<machine_id>[0-9]+)/', page_edit, name='page_edit'),
     url(r'^send_message/(?P<machine_id>[0-9]+)/', send_message, name='send_message'),
     url(r'^download/(?P<file_id>[0-9]+)/', download, name='download'),
     url(r'^be_mentor/(?P<machine_id>[0-9]+)/', be_mentor, name='be_mentor'),
     url(r'^subscribe/(?P<machine_id>[0-9]+)/', subscribe, name='subscribe'),


]