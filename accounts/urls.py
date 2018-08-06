from django.conf.urls import url
from accounts.views import login, logout, register_user, user_profile,members_directory,members_network,contact_member_message,json_data,map_view,welcome_view
from accounts.views import sciport_view,sciport_subskill_view,subskils,search_text
urlpatterns = [
    url(r'^login/', login, name='auth_login'),
    url(r'^logout/', logout, name='auth_logout'),
    url(r'^register/', register_user, name='auth_register'),
    
    url(r'^profile/', user_profile, name='profile'),
    url(r'^welcome/', welcome_view, name='welcome'),

    url(r'^members/', members_directory, name='members'),
    url(r'^members_network/', members_network, name='members_network'),
    url(r'^contact_member_message/(?P<receiver_id>[0-9]+)/', contact_member_message, name='contact_member_message'),
    url(r'^json_data/', json_data, name='json_data'),
    url(r'^map/', map_view, name='map'),
    url(r'^sciport/',sciport_view, name='sciport'),
    url(r'^sciport_subskill/(.*?)/',sciport_subskill_view, name='sciport_subskill'),
    url(r'^subskils/(?P<skill_id>[0-9]+)/', subskils, name='subskils'),
    url(r'^search_text/', search_text, name='search_text'),
]