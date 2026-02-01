# Analise-de-dados-com-python
Dashboard de Análise de Salários na Área de Dados

Este projeto consiste em um dashboard interativo desenvolvido com Streamlit, cujo objetivo é analisar e visualizar dados salariais da área de dados ao longo dos anos, permitindo explorar tendências, distribuições e comparações entre cargos, países e tipos de trabalho.

O projeto foi desenvolvido com foco em análise exploratória de dados (EDA), visualização interativa e boas práticas de organização de código, sendo ideal para fins de aprendizado, portfólio e demonstração técnica.

🎯 Objetivos do Projeto

Analisar a evolução dos salários na área de dados ao longo do tempo

Comparar salários entre diferentes cargos e senioridades

Identificar padrões geográficos de remuneração

Avaliar o impacto do trabalho remoto e do tipo de contrato

Criar um dashboard interativo e intuitivo para exploração dos dados

🧩 Funcionalidades

📌 Filtros dinâmicos por:

Ano

Senioridade

Tipo de contrato

Tamanho da empresa

📊 Métricas (KPIs):

Salário médio

Salário máximo

Total de registros

Cargo mais frequente

Média salarial por país

📈 Visualizações interativas:

Gráfico de área com evolução salarial ao longo do tempo

Gráfico de barras com os cargos mais bem pagos

Histograma da distribuição salarial

Boxplot da distribuição salarial por cargo

Gráfico de rosca sobre tipos de trabalho (remoto, híbrido, presencial)

Mapa (choropleth) com salário médio de Data Scientists por país

📋 Tabela detalhada com os dados filtrados

🛠️ Tecnologias Utilizadas

Python 3

Streamlit – criação do dashboard interativo

Pandas – manipulação e análise de dados

Plotly Express – visualizações interativas

Git & GitHub – versionamento e compartilhamento

📂 Estrutura do Projeto
├── app.py          # Código principal do dashboard
├── README.md       # Documentação do projeto
└── requirements.txt (opcional)

▶️ Como Executar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2️⃣ Criar e ativar o ambiente virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / Mac
source .venv/bin/activate

3️⃣ Instalar as dependências
pip install streamlit pandas plotly

4️⃣ Executar o dashboard
streamlit run app.py

📊 Fonte dos Dados

Os dados utilizados neste projeto são públicos e foram obtidos a partir do seguinte repositório:

Dataset de salários na área de dados
(utilizado apenas para fins educacionais e analíticos)

🧠 Aprendizados e Conceitos Aplicados

Análise exploratória de dados (EDA)

Uso de filtros interativos em dashboards

Escolha adequada de gráficos para diferentes tipos de análise

Tratamento de dados vazios e exceções

Organização e legibilidade de código em projetos Python

🚀 Próximos Passos (Ideias de Evolução)

Comparação salarial entre trabalho remoto e presencial

Análise de senioridade ao longo do tempo

Deploy do projeto no Streamlit Cloud

Criação de insights automáticos no dashboard

Inclusão de testes e validações de dados

👤 Autor

Projeto desenvolvido por Felipe Soares
📌 Área de interesse: Dados, Tecnologia e Análise de Informação
