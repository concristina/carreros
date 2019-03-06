from django.conf.urls import url
from .views import elegir_adjunto, AsignarMesaAdjunto, editar_foto

urlpatterns = [
    url(r'^$', elegir_adjunto, name="elegir-adjunto"),
    url(r'^(?P<attachment_id>\d+)/$', AsignarMesaAdjunto.as_view(), name='asignar-mesa'),
    url(r'^(?P<attachment_id>\d+)/editar-foto$', editar_foto, name='editar-foto'),
]
