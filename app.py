import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard de Veículos", layout="wide")

st.header("Dashboard de Anúncios de Carros")
st.write("Aplicativo web desenvolvido com Streamlit para analisar anúncios de veículos.")

@st.cache_data
def carregar_dados():
    dados = pd.read_csv("vehicles_us.csv")
    return dados

car_data = carregar_dados()

st.subheader("Visualização inicial dos dados")
st.dataframe(car_data.head(10))

st.subheader("Filtros")
col_filtro1, col_filtro2 = st.columns(2)

with col_filtro1:
    tipos = sorted(car_data["type"].dropna().unique())
    tipo_escolhido = st.multiselect("Escolha o tipo de veículo:", tipos, default=tipos)

with col_filtro2:
    condicoes = sorted(car_data["condition"].dropna().unique())
    condicao_escolhida = st.multiselect("Escolha a condição:", condicoes, default=condicoes)

dados_filtrados = car_data[
    (car_data["type"].isin(tipo_escolhido)) &
    (car_data["condition"].isin(condicao_escolhida))
]

st.subheader("Indicadores gerais")
col1, col2, col3 = st.columns(3)
col1.metric("Quantidade de anúncios", len(dados_filtrados))
col2.metric("Preço médio", f"US$ {dados_filtrados['price'].mean():,.2f}")
col3.metric("Odômetro médio", f"{dados_filtrados['odometer'].mean():,.0f} mi")

st.subheader("Gráficos interativos")

build_hist_price = st.checkbox("Criar histograma de preços")
if build_hist_price:
    st.write("Criando um histograma para a coluna price.")
    fig = px.histogram(dados_filtrados, x="price", nbins=30, title="Distribuição dos preços dos veículos")
    st.plotly_chart(fig, use_container_width=True)

build_hist_odometer = st.checkbox("Criar histograma de odômetro")
if build_hist_odometer:
    st.write("Criando um histograma para a coluna odometer.")
    fig = px.histogram(dados_filtrados, x="odometer", nbins=30, title="Distribuição da quilometragem")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox("Criar gráfico de dispersão")
if build_scatter:
    st.write("Criando um gráfico de dispersão entre preço e odômetro.")
    fig = px.scatter(
        dados_filtrados,
        x="odometer",
        y="price",
        color="condition",
        hover_data=["model", "model_year", "type"],
        title="Relação entre preço e quilometragem"
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Conclusão")
st.write(
    "Este dashboard ajuda a observar padrões dos anúncios, como a distribuição dos preços, "
    "a quilometragem dos veículos e a relação entre preço, condição e odômetro."
)
