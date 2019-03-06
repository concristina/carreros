from elecciones.models import Mesa
from adjuntos.models import Attachment


def contadores(request):
    return {
        'adjuntos_count': Attachment.sin_asignar().count(),
        'mesas_count': Mesa.con_carga_pendiente().count(),
    }
