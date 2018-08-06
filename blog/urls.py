from django.conf.urls import url
from blog.views import content_view,content_save,comment_save

urlpatterns = [   
     url(r'^content/', content_view, name='content'),
     url(r'^content_save/', content_save, name='content_save'),
     url(r'^comment_save/', comment_save, name='comment_save'),
]