"""
URL configuration for PGTrips project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path,include
from PGTapp.views import CustomLoginView
from rest_framework import routers, serializers,viewsets
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='inicio_sesion'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',include('PGTapp.urls')),
    path('',include('reservaciones.urls')),
    path('', include('PGaleria.urls')),
    path('docs/', include_docs_urls(title='documentacion'), name='docs'), 
]
# Los serializers definen la representacion de la API:
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')

#Las Viewsets definen el comportamiento de la vista 
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Los routers proveen un camino facil para determinar la url conf
router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

#Conectar nuestra API usando el automatic url routing
#adicionalmente, incluimos el login URLs para la navegacion en la API

urlpatterns += [path(r'', include(router.urls)),
               path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')) ]
