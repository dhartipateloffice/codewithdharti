from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('lang/<slug:slug>/', views.lang_detail, name='lang-detail'),
    path('subtopic/<slug:slug>/', views.subtopic_detail, name='subtopic-detail'),

    path('tutorial/', views.tutorial, name='tutorial'),
    path('notes/', views.notes, name='notes'),
    path('blog/', views.blog, name='blog'),

    path('codegallary/', views.codegallary, name='codegallary'),
    path('contact/', views.contact, name='contact'),


    path('python_tutorial/', views.python_tutorial, name='python_tutorial'),
    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)