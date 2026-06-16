# Dashboard de Anúncios de Carros

Este projeto apresenta uma análise exploratória simples de anúncios de veículos usando Python, Pandas, Plotly Express e Streamlit.

O aplicativo web permite visualizar informações do conjunto de dados `vehicles_us.csv`, como distribuição de preços, quilometragem, ano do veículo e relação entre preço e odômetro.

## Funcionalidades

- Visualização inicial dos dados em tabela.
- Indicadores gerais do conjunto de dados.
- Histograma interativo de preços.
- Histograma interativo de odômetro.
- Gráfico de dispersão entre preço e odômetro.
- Filtros por tipo de veículo e condição.

## Arquivos do projeto

- `app.py`: arquivo principal do aplicativo Streamlit.
- `vehicles_us.csv`: conjunto de dados utilizado na análise.
- `requirements.txt`: bibliotecas necessárias para executar o projeto.
- `notebooks/EDA.ipynb`: notebook com análise exploratória inicial.
- `.streamlit/config.toml`: configuração necessária para publicação no Render.

## Como executar localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o aplicativo:

```bash
streamlit run app.py
```

## Deploy no Render

Build Command:

```bash
pip install --upgrade pip && pip install -r requirements.txt
```

Start Command:

```bash
streamlit run app.py
```



URL do aplicativo:# Projeto Streamlit Vehicles

Aplicativo desenvolvido com Streamlit para análise exploratória de dados de veículos.

## Link da aplicação

https://projeto-streamlit-vehicles.onrender.com