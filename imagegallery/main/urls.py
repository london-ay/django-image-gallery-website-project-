from django.urls import path
from . import views


urlpatterns = [
    path('', views.photos, name='photos'),
    path('errorpage', views.errorpage),
    path('contact', views.contact, name='contact'),
]