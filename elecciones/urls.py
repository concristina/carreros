# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from fancy_cache import cache_page


cached = cache_page(600)


urlpatterns = [
    url('^escuelas.geojson$', cached(views.LugaresVotacionGeoJSON.as_view()), name='geojson'),
    url('^escuelas/(?P<pk>\d+)$', views.EscuelaDetailView.as_view(), name='detalle_escuela'),
    url('^mapa/$', cached(views.Mapa.as_view()), name='mapa'),

    url('^proyecciones/(?P<eleccion_id>\d+)/$', views.ResultadosProyectadosEleccion.as_view(), name='proyecciones'),

    url('^resultadospk/$', views.ResultadosEleccion.as_view(), { "template_name" : "elecciones/resultadospk.html"}, name='resultados-pk-eleccion'),
    url('^resultados/$', views.ResultadosEleccion.as_view(), name='resultados-eleccion'),

    url(r'^fiscal_mesa/', views.fiscal_mesa, name='fiscal_mesa'),
]
