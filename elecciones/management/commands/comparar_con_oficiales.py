import json

from django.conf import settings

from elecciones.models import Mesa, Opcion, VotoMesaReportado

from elecciones.management.commands.importar_carta_marina import CarrerosBaseCommand



class Command(CarrerosBaseCommand):
    help = "Comparar con los resutlados oficiales"

    def add_arguments(self, parser):
        parser.add_argument(
            'dump_resultados', default='./resultados.json')

    def handle(self, *args, **options):
        with open(options['dump_resultados']) as fh:
            oficiales = json.load(fh)

        opciones = Opcion.objects.order_by('orden').all()
        for mesa in Mesa.objects.all():

            res = oficiales.get(str(mesa.numero))
            if res is None:
                print(f'No hay datos oficiales para la mesa: {mesa.numero}')
                continue
            hay_discrepancia = hay_votos = False
            for i, opcion in enumerate(opciones):
                try:
                    votos = VotoMesaReportado.objects.get(mesa=mesa, opcion=opcion).votos
                except VotoMesaReportado.DoesNotExist:
                    pass
                else:
                    hay_votos = True
                    if votos != res[i]:
                        hay_discrepancia = True
                        print(f'** DISCREPANCIA **: {mesa}, {opcion}, fiscal: {votos}, '
                              f'oficial: {res[i]}')
            if (not hay_discrepancia) and hay_votos:
                print(f"Mesa: {mesa.numero} concuerda con oficial.")