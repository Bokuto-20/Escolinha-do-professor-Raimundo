from django.contrib import admin
from .models import Periodo, Oracao, ComponenteSintatico

# Inline para Oracao dentro de Periodo
class OracaoInline(admin.StackedInline):
    model = Oracao
    extra = 1
    # Removido o ComponenteSintaticoInline daqui

# Admin para Periodo
@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto_original', 'tipo_periodo', 'data_criacao')
    search_fields = ('texto_original',)
    list_filter = ('tipo_periodo', 'data_criacao')
    inlines = [OracaoInline]

# Admin para Oracao
@admin.register(Oracao)
class OracaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'periodo', 'tipo_oracao', 'oracao_principal')
    list_filter = ('tipo_oracao', 'periodo')
    search_fields = ('texto_oracao',)
    # Removido o ComponenteSintaticoInline daqui

# Admin para ComponenteSintatico (agora registrado separadamente)
@admin.register(ComponenteSintatico)
class ComponenteSintaticoAdmin(admin.ModelAdmin):
    list_display = ('oracao', 'tipo_componente', 'classificacao', 'texto_componente')
    list_filter = ('tipo_componente', 'classificacao')
    search_fields = ('texto_componente',)
    list_editable = ('tipo_componente', 'classificacao', 'texto_componente')
    list_per_page = 20
