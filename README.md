# Analise-de-dados-com-python
📊 Dashboard de Salários na Área de Dados

Este projeto apresenta um dashboard interativo desenvolvido em Python com Streamlit, voltado para a análise salarial na área de dados.
O objetivo é permitir a exploração de informações como salário médio, distribuição por cargo, tendências ao longo dos anos, localização geográfica e tipos de trabalho, de forma simples e visual.

O projeto também serve como exemplo prático de:

Criação e uso de ambientes virtuais em Python

Organização de dependências com requirements.txt

Boas práticas para execução de aplicações Streamlit

🎯 Objetivo do Projeto

Analisar salários na área de dados ao longo do tempo

Comparar cargos e níveis de experiência

Visualizar distribuições salariais de forma clara

Criar um dashboard interativo para análise exploratória

Demonstrar boas práticas de configuração de ambiente Python

🛠️ Tecnologias Utilizadas

Python 3

Streamlit – Interface e dashboard interativo

Pandas – Manipulação e análise de dados

Plotly – Visualizações interativas

Git & GitHub – Versionamento e documentação

🧪 Criação do Ambiente Virtual

Para evitar conflitos de dependências e garantir um ambiente isolado, é recomendado utilizar um ambiente virtual Python.

🔹 Criar o ambiente virtual
python3 -m venv .venv

🔹 Ativar o ambiente virtual

O comando varia conforme o sistema operacional.

Windows (PowerShell / VS Code):

.venv\Scripts\Activate


Linux / macOS:

source .venv/bin/activate

⚠️ Observação Importante (Windows)

O Windows costuma bloquear scripts de execução, o que pode impedir a ativação do ambiente virtual.

Caso isso ocorra, execute o seguinte comando no PowerShell:

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser


Esse comando libera a execução de scripts locais apenas para o usuário atual.

📦 Gerenciamento de Dependências

Para facilitar a instalação das bibliotecas em qualquer ambiente, o projeto utiliza um arquivo requirements.txt, contendo todas as dependências necessárias.

📄 Exemplo do requirements.txt
pandas==2.2.3
streamlit==1.44.1
plotly==5.24.1

📥 Instalar todas as dependências
pip install -r requirements.txt


O parâmetro -r indica que o pip deve instalar todas as bibliotecas listadas no arquivo.

🧱 Configuração Base da Página (Streamlit)

A configuração inicial do dashboard define o título, ícone e layout da aplicação:

# Configuração básica da página
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)


Essa configuração garante:

Layout em tela cheia

Identidade visual consistente

Melhor experiência para análise de dados

▶️ Executando o Projeto

Com o ambiente virtual ativado e as dependências instaladas, execute o projeto via PowerShell ou terminal:

streamlit run app.py


Após o comando, o Streamlit abrirá automaticamente o dashboard no navegador.

📊 Funcionalidades do Dashboard

📌 Filtros interativos por ano, cargo e outros critérios

📈 Gráficos de tendência salarial

📦 Boxplot de distribuição salarial por cargo

🌍 Análise salarial por país

📊 Métricas resumidas (KPIs)

📋 Visualização tabular dos dados filtrados

📂 Estrutura do Projeto
├── app.py              # Código principal do dashboard
├── requirements.txt    # Lista de dependências
└── README.md           # Documentação do projeto

🧠 Conceitos Aplicados

Ambientes virtuais em Python

Análise exploratória de dados (EDA)

Visualização de dados interativa

Boas práticas de organização de projeto

Uso profissional do Streamlit

🚀 Possíveis Evoluções

Deploy no Streamlit Cloud

Comparação entre trabalho remoto, híbrido e presencial

Análise por senioridade ao longo do tempo

Inclusão de insights automáticos no dashboard

👤 Autor

Projeto desenvolvido por Felipe Soares
📌 Interesse em Dados, Tecnologia e Análise de Informação
