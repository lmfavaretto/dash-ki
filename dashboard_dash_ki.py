import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table

# Carregar os dados (substitua pelo caminho correto se necessário)
df_clusters = pd.read_csv("clusters_clientes.csv")
df_sazonalidade = pd.read_csv("sazonalidade_dias.csv")
df_faixa_etaria = pd.read_csv("faixa_etaria.csv")
df_faixa_pedidos = pd.read_csv("faixa_pedidos.csv")
df_rfm = pd.read_csv("rfm_matriz.csv")

# Criar a aplicação Dash
app = Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    html.H1("Dashboard de Análise de Clientes - Restaurante Ki", style={'textAlign': 'center'}),

    html.H3("Clusterização de Clientes por Quantidade de Pedidos"),
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df_clusters.columns],
        data=df_clusters.to_dict("records"),
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center'},
    ),

    html.H3("Sazonalidade por Dia da Semana"),
    dcc.Graph(
        df_sazonalidade = df_sazonalidade.to_frame().rename(columns={0: "Número de Pedidos"}).reset_index()
figure=px.bar(df_sazonalidade, x='Dia da Semana', y="Número de Pedidos",


                      title="Pedidos por Dia da Semana")
    ),

    html.H3("Distribuição de Clientes por Faixa Etária"),
    dcc.Graph(
        figure=px.pie(df_faixa_etaria, names='Faixa Etária', values='Percentual',
                      title="Distribuição de Clientes por Idade")
    ),

    html.H3("Clusterização de Faixa Etária por Ticket Médio e Número de Pedidos"),
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df_faixa_pedidos.columns],
        data=df_faixa_pedidos.to_dict("records"),
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center'},
    ),

    html.H3("Matriz RFM dos Clientes"),
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df_rfm.columns],
        data=df_rfm.to_dict("records"),
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center'},
    ),

    html.H3("Distribuição de Clientes por RFM Score"),
    dcc.Graph(
        figure=px.bar(df_rfm['RFM Score'].value_counts().sort_index().reset_index(),
                      x='index', y='RFM Score',
                      labels={'index': 'RFM Score', 'RFM Score': 'Número de Clientes'},
                      title="Distribuição de RFM Score")
    )
])

# Rodar o servidor do Dash
if __name__ == '__main__':
    app.run_server(debug=True)
