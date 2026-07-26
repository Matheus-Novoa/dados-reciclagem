import streamlit as st

from data_utils import carregar_dados
from ui import (
    CSS_STYLES,
    render_dashboard_header,
    render_section_title,
    render_data_table,
)


st.set_page_config(
    page_title="Catálogo de Empresas de Reciclagem",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(CSS_STYLES, unsafe_allow_html=True)
render_dashboard_header("Catálogo de Empresas de Reciclagem")

df_original = carregar_dados()

show_columns = ["empresa", "nome_municipio", "uf", "regiao", "desc_porte_empresa"]
df_show = df_original[show_columns]

# # Summary metrics
# metric_empresas = df_original["empresa"].nunique()
# metric_estados = df_original["uf"].nunique()
# metric_municipios = df_original["nome_municipio"].nunique()
# metric_regioes = df_original["regiao"].nunique()

# render_metrics_section([
#     ("Empresas", metric_empresas, "Total de empresas cadastradas"),
#     ("Estados", metric_estados, "Estados com presença de empresas"),
#     ("Municípios", metric_municipios, "Municípios com empresas de reciclagem"),
#     ("Regiões", metric_regioes, "Regiões brasileiras contempladas"),
# ])

valor_padrao = "TODOS"

render_section_title("Filtros de busca")

col_f1, col_f2, col_f3, col_f4 = st.columns(4, gap="large")

with col_f1:
    opcoes_regiao = [valor_padrao] + [str(valor) for valor in df_show["regiao"].dropna().unique()]
    filtro_regiao = st.selectbox("Região", options=opcoes_regiao)

with col_f2:
    opcoes_estado = [valor_padrao] + [str(valor) for valor in df_show["uf"].dropna().unique()]
    filtro_estado = st.selectbox("Estado", options=opcoes_estado)

with col_f3:
    opcoes_cidade = [valor_padrao] + [str(valor) for valor in df_show["nome_municipio"].dropna().unique()]
    filtro_cidade = st.selectbox("Cidade", options=opcoes_cidade)

with col_f4:
    opcoes_porte = [valor_padrao] + [str(valor) for valor in df_show["desc_porte_empresa"].dropna().unique()]
    filtro_porte = st.selectbox("Porte", options=opcoes_porte)

df_filtrado = df_show.copy()

if filtro_regiao != valor_padrao:
    df_filtrado = df_filtrado[df_filtrado["regiao"] == filtro_regiao]

if filtro_estado != valor_padrao:
    df_filtrado = df_filtrado[df_filtrado["uf"] == filtro_estado]

if filtro_cidade != valor_padrao:
    df_filtrado = df_filtrado[df_filtrado["nome_municipio"] == filtro_cidade]

if filtro_porte != valor_padrao:
    df_filtrado = df_filtrado[df_filtrado["desc_porte_empresa"] == filtro_porte]

render_data_table(
    df_filtrado,
    columns=["empresa", "nome_municipio", "uf", "regiao", "desc_porte_empresa"],
    column_labels={
        "empresa": "Empresa",
        "nome_municipio": "Cidade",
        "uf": "Estado",
        "regiao": "Região",
        "desc_porte_empresa": "Porte",
    },
)
