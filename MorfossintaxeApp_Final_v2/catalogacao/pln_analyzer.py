import spacy
import json

# Carregar o modelo de português
try:
    nlp = spacy.load("pt_core_news_sm")
except OSError:
    print("Modelo 'pt_core_news_sm' não encontrado. Certifique-se de que foi baixado.")
    nlp = None

def get_subtree_text(token):
    """Retorna o texto completo da subárvore de um token, ordenado pela posição."""
    return " ".join([t.text for t in sorted(token.subtree, key=lambda t: t.i)]).strip()

def analyze_periodo(text):
    """
    Realiza a análise sintática de um período usando spaCy, com foco em Sujeito, Predicado e Complementos/Adjuntos.
    """
    if nlp is None:
        return {"error": "Modelo de PLN não carregado."}

    doc = nlp(text)
    
    oracoes_data = []
    oracao_id_counter = 1
    
    for sent in doc.sents:
        root = None
        for token in sent:
            if token.dep_ == "ROOT":
                root = token
                break
        
        if root is None:
            continue

        # Lista de tokens que já foram identificados como parte de um componente (Sujeito, Complementos, Adjuntos)
        used_tokens = set()

        # --- 1. Identificação do Sujeito ---
        sujeito_tokens = []
        for token in sent:
            if token.dep_ == "nsubj" and token.head == root:
                sujeito_tokens.append(token)
                used_tokens.update(token.subtree)
                break
        
        sujeito_text = ""
        sujeito_classificacao = ""
        
        if sujeito_tokens:
            sujeito_text = get_subtree_text(sujeito_tokens[0])
            sujeito_classificacao = "Simples (PLN)"
        else:
            sujeito_text = "Sujeito Oculto/Indeterminado"
            sujeito_classificacao = "Oculto/Indeterminado (PLN)"

        # --- 2. Identificação de Outros Componentes (Complementos e Adjuntos) ---
        outros_componentes = []
        
        # Dependências a serem consideradas como componentes adicionais
        componente_deps = {
            "obj": "Objeto Direto/Indireto",
            "obl": "Adjunto Adverbial",
            "nmod": "Complemento Nominal/Adjunto Adnominal",
            "advmod": "Adjunto Adverbial (Modificador)"
        }
        
        for token in sent:
            # Verifica se o token é um modificador do verbo principal (ROOT)
            if token.head == root and token.dep_ in componente_deps:
                componente_text = get_subtree_text(token)
                
                # Evita duplicidade com o sujeito
                if token not in used_tokens:
                    outros_componentes.append({
                        "tipo_componente": componente_deps[token.dep_],
                        "texto_componente": componente_text,
                        "classificacao": f"Identificado por {token.dep_}"
                    })
                    used_tokens.update(token.subtree)
        
        # --- 3. Identificação do Predicado ---
        # O predicado é o verbo principal e seus auxiliares.
        predicado_text = get_subtree_text(root)
        predicado_classificacao = "Verbal (PLN)"
        
        # --- 4. Montagem da Oração ---
        
        componentes_list = [
            {
                "tipo_componente": "SUJEITO",
                "texto_componente": sujeito_text,
                "classificacao": sujeito_classificacao
            },
            {
                "tipo_componente": "PREDICADO",
                "texto_componente": predicado_text,
                "classificacao": predicado_classificacao
            }
        ] + outros_componentes
        
        oracao_data = {
            "id": oracao_id_counter,
            "texto_oracao": sent.text.strip(),
            "tipo_oracao": "PRINCIPAL (PLN)",
            "componentes": componentes_list,
            "subordinadas": []
        }
        
        oracoes_data.append(oracao_data)
        oracao_id_counter += 1

    # --- 5. Mapeamento Hierárquico (Simplificação) ---
    estrutura_sintatica = []
    for data in oracoes_data:
        estrutura_sintatica.append({
            "oracao": data,
            "componentes": data["componentes"],
            "subordinadas": []
        })

    return {
        "texto_original": text,
        "tipo_periodo": "COMPOSTO (PLN)" if len(oracoes_data) > 1 else "SIMPLES (PLN)",
        "estrutura_sintatica": estrutura_sintatica
    }

# Exemplo de uso (para testes internos)
if __name__ == '__main__':
    texto_teste = "O aluno estudou a matéria com dedicação na biblioteca."
    analise = analyze_periodo(texto_teste)
    print(json.dumps(analise, indent=4, ensure_ascii=False))
