from django.db import models

# 1. Modelo para o Período (simples ou composto)
class Periodo(models.Model):
    texto_original = models.TextField(
        verbose_name="Texto do Período",
        help_text="O período completo a ser analisado."
    )
    tipo_periodo = models.CharField(
        max_length=10,
        choices=[('SIMPLES', 'Simples'), ('COMPOSTO', 'Composto')],
        default='SIMPLES',
        verbose_name="Tipo de Período"
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Período {self.id}: {self.texto_original[:50]}..."

    class Meta:
        verbose_name = "Período"
        verbose_name_plural = "Períodos"

# 2. Modelo para a Oração (componente do Período)
class Oracao(models.Model):
    periodo = models.ForeignKey(
        Periodo,
        on_delete=models.CASCADE,
        related_name='oracoes',
        verbose_name="Período de Origem"
    )
    texto_oracao = models.TextField(
        verbose_name="Texto da Oração",
        help_text="O trecho da oração dentro do período."
    )
    # Classificação Morfológica (Tipo de Oração)
    tipo_oracao = models.CharField(
        max_length=50,
        choices=[
            ('PRINCIPAL', 'Principal'),
            ('COORDENADA', 'Coordenada'),
            ('SUBORDINADA_SUBSTANTIVA', 'Subordinada Substantiva'),
            ('SUBORDINADA_ADJETIVA', 'Subordinada Adjetiva'),
            ('SUBORDINADA_ADVERBIAL', 'Subordinada Adverbial'),
            ('REDUZIDA', 'Reduzida')
        ],
        default='PRINCIPAL',
        verbose_name="Tipo de Oração"
    )
    # Para mapeamento hierárquico (Subordinadas)
    oracao_principal = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinadas',
        verbose_name="Oração Principal/Regente"
    )

    def __str__(self):
        return f"Oração {self.id} ({self.tipo_oracao}): {self.texto_oracao[:50]}..."

    class Meta:
        verbose_name = "Oração"
        verbose_name_plural = "Orações"

# 3. Modelo para os Componentes Sintáticos Essenciais (Sujeito e Predicado)
class ComponenteSintatico(models.Model):
    oracao = models.ForeignKey(
        Oracao,
        on_delete=models.CASCADE,
        related_name='componentes',
        verbose_name="Oração"
    )
    tipo_componente = models.CharField(
        max_length=10,
        choices=[('SUJEITO', 'Sujeito'), ('PREDICADO', 'Predicado')],
        verbose_name="Tipo de Componente"
    )
    texto_componente = models.TextField(
        verbose_name="Texto do Componente",
        help_text="O trecho que corresponde ao sujeito ou predicado."
    )
    # Classificação Sintática do Sujeito/Predicado
    classificacao = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Classificação Detalhada",
        help_text="Ex: Simples, Composto, Oculto, Indeterminado (para Sujeito); Verbal, Nominal, Verbo-Nominal (para Predicado)."
    )

    def __str__(self):
        return f"{self.tipo_componente}: {self.texto_componente[:50]}..."

    class Meta:
        verbose_name = "Componente Sintático"
        verbose_name_plural = "Componentes Sintáticos"
        unique_together = ('oracao', 'tipo_componente') # Garante no máximo 1 Sujeito e 1 Predicado por Oração
