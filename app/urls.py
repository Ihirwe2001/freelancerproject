from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('Business/', views.Business, name='Business'),
    path('freelance/', views.freelance, name='freelance'),
    path('free1/', views.free1, name='free1'),
    path('free2/', views.free2, name='free2'),
    path('free3/', views.free3, name='free3'),
    path('free4/', views.free4, name='free4'),
    path('free5/', views.free5, name='free5'),
    path('free6/', views.free6, name='free6'),
    path('free7/', views.free7, name='free7'),
    path('free8/', views.free8, name='free8'),
    path('free9/', views.free9, name='free9'),
    path('graphic/', views.graphic, name='graphic'),
    path('back/', views.back, name='back'),
    path('analyst/', views.analyst, name='analyst'),
    path('frontend/', views.frontend, name='frontend'),
    path('reg2/', views.reg2, name='reg2'),
    path('freelreg/', views.freelreg, name='freelreg'),
    path('customer/', views.customer, name='customer'),
    path('partener/', views.partener, name='partener'),
   
   
   
]

