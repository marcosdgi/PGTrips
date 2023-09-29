from django.urls import path, include
from PGTapp.views import *
from PGTapp.views import CustomLoginView
urlpatterns = [
   
    path('', base ),
    path('home/',homepage, name='home'),
    path ('login/', CustomLoginView.as_view(),name ='login'),
    path ('programacion/', programacion, name='programacion'),
    path ('informacion/', informacion, name='informacion' ),

]
