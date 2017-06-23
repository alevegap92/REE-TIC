from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import PaypalView, PaypalExecuteView,  get_context
from . import views

urlpatterns = [
    url(r'^aceptar-pago/$', login_required(PaypalExecuteView.as_view(),), name="aceptar-pago-paypal"),
    url(r'^pago/(?P<proyecto_pk>\d+)/$', login_required(PaypalView.as_view(),), name="pago-paypal"),
    url(r'^$', views.get_context,  name='proyecto_listar'),
]
