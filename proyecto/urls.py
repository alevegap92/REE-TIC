from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from proyecto import views
<<<<<<< HEAD
from proyecto.views import proyectoList, proyectoCreate, proyectoUpdate, proyectoDelete, proyectoDetail, index, proyectoList2, agregar_comentario

urlpatterns = [
    #url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(proyectoCreate.as_view()), name='proyecto_crear'),
    #url(r'^listar$', proyectoList.as_view(), name='proyecto_listar'),
=======
from proyecto.views import proyectoList, proyectoCreate, proyectoUpdate, proyectoDelete, proyectoDetail, index, proyectoList2

urlpatterns = [
    url(r'^nuevo$', login_required(proyectoCreate.as_view()), name='proyecto_crear'),
>>>>>>> e2ceb4a335e393d6f7eb3dc5bded029d1816553f
    url(r'^$', proyectoList.as_view(), name='proyecto_listar'),
    url(r'^todos$', proyectoList2.as_view(), name='proyecto_listar0'),
    url(r'^(?P<pk>\d+)$', proyectoDetail.as_view(), name='proyecto_detalle'),
    url(r'^(?P<pk>\d+)/editar$', login_required(proyectoUpdate.as_view()), name='proyecto_editar'),
    url(r'^(?P<pk>\d+)/eliminar/$', login_required(proyectoDelete.as_view()), name='proyecto_eliminar'),
<<<<<<< HEAD
    url(r'^(?P<pk>\d+)/comentar/$', views.agregar_comentario, name='agregar_comentario'),
=======
>>>>>>> e2ceb4a335e393d6f7eb3dc5bded029d1816553f
]
