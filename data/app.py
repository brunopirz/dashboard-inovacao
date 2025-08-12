import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import config

# Criar conexão com PostgreSQL
def get_connection():
    engine = create_engine(
        f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    )
    return engine

# Carregar dados
@st.cache_data
def load_data():
    engine = get_connection()
    query = "SELECT * FROM projetos_inovacao"
    df = pd.read_sql(query, engine)
    return df

st.set_page_config(page_title="Dashboard de Inovação", layout="wide")

st.title("📊 Dashboard de Inovação")
st.markdown("Visualize métricas e indicadores de inovação tecnológica.")

df = load_data()

# Filtros
categorias = st.sidebar.multiselect("Categoria", df["categoria"].unique())
status = st.sidebar.multiselect("Status", df["status"].unique())

df_filtrado = df.copy()
if categorias:
    df_filtrado = df_filtrado[df_filtrado["categoria"].isin(categorias)]
if status:
    df_filtrado = df_filtrado[df_filtrado["status"].isin(status)]

# Gráfico de linha
col1, col2 = st.columns(2)
with col1:
    fig_tempo = px.line(df_filtrado, x="data_inicio", y="orcamento", color="categoria", title="Orçamento ao Longo do Tempo")
    st.plotly_chart(fig_tempo, use_container_width=True)

# Gráfico de pizza
with col2:
    fig_status = px.pie(df_filtrado, names="status", title="Distribuição por Status")
    st.plotly_chart(fig_status, use_container_width=True)

# Tabela
st.subheader("📋 Lista de Projetos")
st.dataframe(df_filtrado)

