# MorfossintaxeApp: Ferramenta de Análise Morfossintática

Este projeto é uma aplicação web robusta, desenvolvida em **Django**, projetada para auxiliar na **catalogação e análise da estrutura morfossintática** de períodos e orações da língua portuguesa. A ferramenta combina a capacidade de **análise manual** detalhada com a **análise automática** via Processamento de Linguagem Natural (PLN), tornando-a ideal para estudos linguísticos, educacionais ou de pesquisa.

## 🌟 Funcionalidades Principais

*   **Catalogação de Períodos:** Permite o registro e a gestão de períodos textuais para análise.
*   **Análise Sintática Hierárquica:** Exibe a estrutura completa de um período, mapeando as **Orações Principais** e suas respectivas **Orações Subordinadas** de forma recursiva.
*   **Identificação de Componentes:** Detalha os **Componentes Sintáticos** (sujeito, predicado, complementos, etc.) de cada oração.
*   **Modo de Análise Dupla:**
    *   **Análise Manual:** Permite a inserção e a classificação detalhada dos componentes por um usuário.
    *   **Análise Automática (PLN):** Integra módulos de PLN (como `spaCy` ou similar, conforme as dependências) para realizar a análise sintática de forma automatizada, agilizando o processo.
*   **Visualização Detalhada:** Apresenta uma interface amigável para a visualização da estrutura sintática complexa.

## 💻 Tecnologias Utilizadas

O projeto é construído sobre uma pilha de tecnologias amplamente utilizadas e robustas:

| Categoria | Tecnologia | Descrição |
| :--- | :--- | :--- |
| **Backend** | **Python** | Linguagem de programação principal. |
| **Framework Web** | **Django** | Framework de alto nível para desenvolvimento rápido e seguro. |
| **Banco de Dados** | `db.sqlite3` (Padrão) | Banco de dados inicial, facilmente configurável para PostgreSQL ou MySQL. |
| **PLN** | **spaCy** e dependências relacionadas | Utilizado para o processamento e análise automática de textos. |
| **Frontend** | **HTML/CSS/JavaScript** | Estrutura e interatividade da interface do usuário (provavelmente utilizando *templates* do Django). |

## 🚀 Como Executar o Projeto Localmente

Para configurar e rodar o `MorfossintaxeApp` em seu ambiente local, siga os passos abaixo:

### 1. Pré-requisitos

Certifique-se de ter o **Python 3.x** e o `pip` instalados.

### 2. Instalação

Clone o repositório e navegue até o diretório do projeto:

```bash
# Substitua 'seu-repositorio' pelo nome real do seu repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Crie e ative um ambiente virtual (recomendado):

```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# venv\Scripts\activate  # No Windows
```

Instale as dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Configuração do Banco de Dados

Execute as migrações do Django para criar o esquema do banco de dados:

```bash
python manage.py migrate
```

### 4. Acesso ao Painel Administrativo

Se você estiver utilizando o arquivo `db.sqlite3` fornecido, o acesso ao painel administrativo do Django (`/admin`) pode ser feito com as seguintes credenciais:

| Campo | Valor |
| :--- | :--- |
| **Nome de Usuário** | `admin` |
| **Senha** | `admin` |

**Nota:** Caso inicie com um banco de dados vazio (após rodar `migrate` sem o `db.sqlite3` original), você precisará criar um superusuário manualmente:

```bash
python manage.py createsuperuser
```

### 5. Execução

Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

O aplicativo estará acessível em `http://127.0.0.1:8000/`.
