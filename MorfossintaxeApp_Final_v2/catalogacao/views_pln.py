from django.shortcuts import render
from .pln_analyzer import analyze_periodo

def analise_automatica(request):
    """
    View para receber o texto do período e exibir a análise sintática automática.
    """
    analise_resultado = None
    texto_entrada = ""

    if request.method == 'POST':
        texto_entrada = request.POST.get('texto_periodo', '').strip()
        if texto_entrada:
            analise_resultado = analyze_periodo(texto_entrada)

    context = {
        'texto_entrada': texto_entrada,
        'analise_resultado': analise_resultado
    }
    return render(request, 'catalogacao/analise_automatica.html', context)
