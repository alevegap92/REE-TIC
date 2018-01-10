"""Configuracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as serve_static_files
from django.contrib import admin
#registro de usuario adaptado
#from django import forms
#from cuentas.forms import ProfileForm
#from registration.backends.default.views import RegistrationView
from cuenta.regbackend import MyRegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^', include('proyecto.urls', namespace='proyecto')),
    #url(r'^notify/', include('paypal.standard.ipn.urls')),
    url(r'^accounts/', include('cuenta.urls', namespace='cuenta')),
    url(r'^', include('pagos.urls')),
    #url(r'^accounts/register/$', RegistrationView.as_view(form_class = ProfileForm), name='registration_register'),
]

if settings.DEBUG:
    urlpatterns += [
    url(
        r'^media/(?P<path>.*)$',
        serve_static_files,
        {'document_root': settings.MEDIA_ROOT}
    )
]
    #urlpatterns += patterns('django.views.static',(r'media/(?P<path>.*)','serve',{'document_root': settings.MEDIA_ROOT}),)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
