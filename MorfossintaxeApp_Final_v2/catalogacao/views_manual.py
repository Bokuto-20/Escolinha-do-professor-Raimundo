from django.shortcuts import render, redirect, get_object_or_404
from .forms import PeriodoForm, OracaoFormSet, ComponenteSintaticoForm
from .models import Periodo, Oracao

# ... (adicionar_periodo_manual view) ...

def adicionar_componente_manual(request, oracao_pk):
    """
    View para adicionar um Componente Sintático a uma Oração específica.
    """
    oracao = get_object_or_404(Oracao, pk=oracao_pk)
    
    if request.method == 'POST':
        form = ComponenteSintaticoForm(request.POST)
        if form.is_valid():
            componente = form.save(commit=False)
            componente.oracao = oracao
            componente.save()
            # Redireciona de volta para a página de detalhes do Período
            return redirect('periodo_detail', pk=oracao.periodo.pk)
    else:
        form = ComponenteSintaticoForm()

    context = {
        'form': form,
        'oracao': oracao,
        'periodo': oracao.periodo,
    }
    return render(request, 'catalogacao/adicionar_componente_manual.html', context)

# O restante da view adicionar_periodo_manual (já existente)
def adicionar_periodo_manual(request):
    """
    View para adicionar um novo período e suas orações em uma única tela.
    """
    if request.method == 'POST':
        form = PeriodoForm(request.POST)
        formset = OracaoFormSet(request.POST, instance=Periodo())
        
        if form.is_valid() and formset.is_valid():
            periodo = form.save()
            formset.instance = periodo
            formset.save()
            return redirect('periodo_detail', pk=periodo.pk)
    else:
        form = PeriodoForm()
        formset = OracaoFormSet(instance=Periodo())

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'catalogacao/adicionar_periodo_manual.html', context)
