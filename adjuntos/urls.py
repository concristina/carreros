from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from .views import elegir_adjunto, AsignarMesaAdjunto, editar_foto, AgregarAdjuntos, agregada

urlpatterns = [
    url(r'^$', elegir_adjunto, name="elegir-adjunto"),
    url(r'^(?P<attachment_id>\d+)/$', AsignarMesaAdjunto.as_view(), name='asignar-mesa'),
    url(r'^(?P<attachment_id>\d+)/editar-foto$', editar_foto, name='editar-foto'),
    url(r'^agregar$', staff_member_required(AgregarAdjuntos.as_view()), name="agregar-adjuntos"),
    url(r'^agregada', agregada, name="agregada"),
]
