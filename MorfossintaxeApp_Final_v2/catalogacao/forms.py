from django import forms
from .models import Periodo, Oracao, ComponenteSintatico
from django.forms import inlineformset_factory

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['texto_original', 'tipo_periodo']
        widgets = {
            'texto_original': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Insira o período completo para análise.'}),
        }

# Forms para as entidades aninhadas (simplificado)
# O ideal seria usar Formsets, mas para simplificar a usabilidade, vamos focar apenas no Periodo por enquanto.

class OracaoForm(forms.ModelForm):
    class Meta:
        model = Oracao
        fields = ['texto_oracao', 'tipo_oracao', 'oracao_principal']
        widgets = {
            'texto_oracao': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Trecho da oração dentro do período.'}),
        }

class ComponenteSintaticoForm(forms.ModelForm):
    class Meta:
        model = ComponenteSintatico
        fields = ['tipo_componente', 'texto_componente', 'classificacao']
        widgets = {
            'texto_componente': forms.TextInput(attrs={'placeholder': 'Ex: O aluno, estudou muito'}),
            'classificacao': forms.TextInput(attrs={'placeholder': 'Ex: Simples, Verbal, etc.'}),
        }

# Formsets para aninhar Orações e Componentes Sintáticos
OracaoFormSet = inlineformset_factory(
    Periodo,
    Oracao,
    form=OracaoForm,
    extra=1,
    can_delete=True
)

ComponenteSintaticoFormSet = inlineformset_factory(
    Oracao,
    ComponenteSintatico,
    form=ComponenteSintaticoForm,
    extra=1,
    can_delete=True
)
