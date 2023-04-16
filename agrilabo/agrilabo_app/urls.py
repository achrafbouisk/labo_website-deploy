from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/details/<int:id>', views.blogDetails, name='blogDetails'),
    path('contact/', views.contact, name='contact'),
    path('merci/', views.merci, name='merci'),
    path('login-client/', views.login_client, name='login_client'),
    # path('maintenance/', views.maintenance, name='maintenance'),
]