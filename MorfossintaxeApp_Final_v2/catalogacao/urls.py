from django.urls import path
from . import views, views_pln, views_manual

urlpatterns = [
    path('', views.periodo_list, name='periodo_list'),
    path('adicionar-manual/', views_manual.adicionar_periodo_manual, name='adicionar_periodo_manual'),
    path('oracao/<int:oracao_pk>/adicionar-componente/', views_manual.adicionar_componente_manual, name='adicionar_componente_manual'),
    path('periodo/<int:pk>/', views.periodo_detail, name='periodo_detail'),
    path('analise-automatica/', views_pln.analise_automatica, name='analise_automatica'),
]
