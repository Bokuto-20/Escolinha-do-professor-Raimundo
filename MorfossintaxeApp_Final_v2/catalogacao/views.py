from django.shortcuts import render, get_object_or_404
from .models import Periodo, Oracao, ComponenteSintatico

def periodo_list(request):
    """Lista todos os períodos catalogados."""
    periodos = Periodo.objects.all().order_by('-data_criacao')
    return render(request, 'catalogacao/periodo_list.html', {'periodos': periodos})

def periodo_detail(request, pk):
    """Exibe os detalhes de um período, incluindo suas orações e componentes sintáticos."""
    periodo = get_object_or_404(Periodo, pk=pk)
    
    # Estrutura para mapeamento hierárquico
    oracoes_principais = periodo.oracoes.filter(oracao_principal__isnull=True)
    
    def get_oracoes_recursivo(oracao):
        """Função recursiva para obter orações subordinadas."""
        oracao_data = {
            'oracao': oracao,
            'componentes': oracao.componentes.all(),
            'subordinadas': []
        }
        for subordinada in oracao.subordinadas.all():
            oracao_data['subordinadas'].append(get_oracoes_recursivo(subordinada))
        return oracao_data

    estrutura_sintatica = []
    for oracao_principal in oracoes_principais:
        estrutura_sintatica.append(get_oracoes_recursivo(oracao_principal))

    context = {
        'periodo': periodo,
        'estrutura_sintatica': estrutura_sintatica,
    }
    return render(request, 'catalogacao/periodo_detail.html', context)
