# ===============================
# IMPORTAÇÕES
# ===============================
import streamlit as st
import pandas as pd
import plotly.express as px


# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)


# ===============================
# CARREGAMENTO DOS DADOS
# ===============================
@st.cache_data
def carregar_dados():
    return pd.read_csv(
        "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"
    )

df = carregar_dados()


# ===============================
# BARRA LATERAL - FILTROS
# ===============================
st.sidebar.header("🔍 Filtros")

anos_selecionados = st.sidebar.multiselect(
    "Ano",
    sorted(df['ano'].unique()),
    default=sorted(df['ano'].unique())
)

senioridades_selecionadas = st.sidebar.multiselect(
    "Senioridade",
    sorted(df['senioridade'].unique()),
    default=sorted(df['senioridade'].unique())
)

contratos_selecionados = st.sidebar.multiselect(
    "Tipo de Contrato",
    sorted(df['contrato'].unique()),
    default=sorted(df['contrato'].unique())
)

tamanhos_selecionados = st.sidebar.multiselect(
    "Tamanho da Empresa",
    sorted(df['tamanho_empresa'].unique()),
    default=sorted(df['tamanho_empresa'].unique())
)


# ===============================
# FILTRAGEM DO DATAFRAME
# ===============================
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]


# ===============================
# TÍTULO PRINCIPAL
# ===============================
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown(
    "Explore os dados salariais na área de dados ao longo dos anos. "
    "Use os filtros à esquerda para refinar sua análise."
)


# ===============================
# MÉTRICAS (KPIs)
# ===============================
st.subheader("📌 Métricas Gerais (Salário anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = len(df_filtrado)
    cargo_mais_frequente = df_filtrado['cargo'].mode()[0]
    salario_por_cargo= (
        df_filtrado.groupby('cargo')['usd']
        .mean()
        .mean
    )

    media_por_pais = (
        df_filtrado.groupby('residencia')['usd']
        .mean()
        .mean()
    )
else:
    salario_medio = salario_maximo = total_registros = media_por_pais = 0
    cargo_mais_frequente = "N/A"

cargo_top = (
    df_filtrado.groupby('cargo')['usd']
    .mean()
    .idxmax()
)

valor_top = (
    df_filtrado.groupby('cargo')['usd']
    .mean()
    .max()
)




# ===============================
# EXIBIÇÃO DAS MÉTRICAS
# ===============================
col1, col2, col3, = st.columns(3)
col4, col5 , col6 = st.columns(3)

col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"{total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)
col5.metric("Média salarial por país", f"${media_por_pais:,.0f}")
col6.metric(
    "Cargo com maior salário médio",
    cargo_top
)
st.markdown("---")


# ===============================
# GRÁFICOS
# ===============================
st.subheader("📊 Análises Visuais")

col_graf1, col_graf2 = st.columns(2)

# --- Gráfico 1: Top 10 cargos por salário médio ---
with col_graf1:
    if not df_filtrado.empty:
        top_cargos = (
            df_filtrado.groupby('cargo')['usd']
            .mean()
            .nlargest(10)
            .sort_values()
            .reset_index()
        )

        fig_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10 cargos por salário médio",
            labels={'usd': 'Salário médio anual (USD)', 'cargo': ''}
        )

        fig_cargos.update_layout(title_x=0.1)
        st.plotly_chart(fig_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir.")


# --- Gráfico 2: Distribuição salarial ---
with col_graf2:
    if not df_filtrado.empty:
        fig_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Salário anual (USD)'}
        )

        fig_hist.update_layout(title_x=0.1)
        st.plotly_chart(fig_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir.")


# ===============================
# SEGUNDA LINHA DE GRÁFICOS
# ===============================
col_graf3, col_graf4 = st.columns(2)

# --- Gráfico 3: Tipo de trabalho ---
with col_graf3:
    if not df_filtrado.empty:
        remoto = df_filtrado['remoto'].value_counts().reset_index()
        remoto.columns = ['Tipo de trabalho', 'Quantidade']

        fig_remoto = px.pie(
            remoto,
            names='Tipo de trabalho',
            values='Quantidade',
            title="Proporção dos tipos de trabalho",
            hole=0.5
        )

        fig_remoto.update_traces(textinfo='percent+label')
        fig_remoto.update_layout(title_x=0.1)
        st.plotly_chart(fig_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir.")


# --- Gráfico 4: Mapa de salários (Data Scientist) ---
with col_graf4:
    df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']

    if not df_ds.empty:
        media_pais = (
            df_ds.groupby('residencia_iso3')['usd']
            .mean()
            .reset_index()
        )

        fig_mapa = px.choropleth(
            media_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='RdYlGn',
            title='Salário médio de Data Scientist por país',
            labels={'usd': 'Salário médio (USD)'}
        )

        fig_mapa.update_layout(title_x=0.1)
        st.plotly_chart(fig_mapa, use_container_width=True)
    else:
        st.warning("Sem dados de Data Scientist para os filtros atuais.")


# ===============================
# GRÁFICO DE ÁREA - TENDÊNCIA
# ===============================
st.subheader("📈 Tendência salarial – Data Scientist")

if not df_ds.empty:
    tendencia = (
        df_ds.groupby('ano', as_index=False)['usd']
        .mean()
    )

    fig_area = px.area(
        tendencia,
        x='ano',
        y='usd',
        title="Evolução do salário médio de Data Scientist",
        labels={'ano': 'Ano', 'usd': 'Salário médio (USD)'}
    )

    fig_area.update_layout(title_x=0.1)
    st.plotly_chart(fig_area, use_container_width=True)
else:
    st.warning("Não há dados suficientes para exibir a tendência.")


st.subheader("📦 Distribuição salarial por cargo")

if not df_filtrado.empty:

    # Define os 5 cargos mais frequentes
    top_cargos = (
        df_filtrado['cargo']
        .value_counts()
        .nlargest(5)
        .index
    )

    # DataFrame usado no boxplot
    df_box = df_filtrado[df_filtrado['cargo'].isin(top_cargos)]

    if not df_box.empty:
        fig_box = px.box(
            df_box,
            x='cargo',
            y='usd',
            title="Distribuição salarial por cargo (Top 5)",
            labels={
                'cargo': 'Cargo',
                'usd': 'Salário anual (USD)'
            }
        )

        fig_box.update_layout(title_x=0.1)
        st.plotly_chart(fig_box, use_container_width=True)

    else:
        st.warning("Não há dados suficientes para os cargos selecionados.")

else:
    st.warning("Nenhum dado disponível para exibir a distribuição salarial.")

# ===============================
# TABELA FINAL
# ===============================
st.subheader("📋 Dados Detalhados")
st.dataframe(df_filtrado)
