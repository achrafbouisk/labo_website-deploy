from django.urls import path
from . import views
from django.views.static import serve
from django.urls import re_path
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/details/<int:id>', views.blogDetails, name='blogDetails'),
    path('contact/', views.contact, name='contact'),
    path('merci/', views.merci, name='merci'),
    path('login-client/', views.login_client, name='login_client'),
    # path('maintenance/', views.maintenance, name='maintenance'),
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
