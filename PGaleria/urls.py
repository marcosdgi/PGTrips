from django.urls import path
from PGaleria.views import *
#importaciones para agregar las url de MEDIA
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path ('galeria/',Galeria , name='galeria'),
    
 ]
#esta linea es para agregar las rutas definidas en el archivo settings 

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)