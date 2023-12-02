import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# Carregar os dados do arquivo 'Financial.xlsx' para um DataFrame
df = pd.read_excel('Financial.xlsx')
df_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Criação dos gráficos inicialmente vazios
chart1 = go.Figure()

# Criando o objeto Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Definição dos widgets
options = [{'label': month, 'value': month} for month in df_month]

multi_select_line_chart = dcc.Dropdown(
    id='multi_select_line_chart',
    options=options,
    value=['Jan'],  # Valor inicial selecionado
    multi=True
)

# Layout do Dash
app.layout = html.Div([
    html.H2('Simple Dashboard With Widgets', style={'color': '#FFFFFF'}),
    
    html.Div([
        html.Div([multi_select_line_chart], className='eight columns'),
        html.Div([dcc.Graph(id='graph1', figure=chart1)], className='eight columns')
    ], className='row'),
    
    # Rodando o app
html.Div([
        dcc.Graph(
            id='data-table',
            figure={
                'data': [
                    {
                        'type': 'table',
                        'header': {
                            'values': df.columns,
                            'align': 'center',
                            'fill': {'color': '#BADFFF'}
                        },
                        'cells': {
                            'values': df.values.T,
                            'align': 'center',
                            'fill': {'color': '#FFDB8'}
                        }
                    }
                ],
                'layout': {
                    'title': "Visualização dos dados em forma Geral"
                }
            }
        )
    ]),

html.Div([
        dcc.Graph(
            id='bar-chart',
            figure={
                'data': [
                    {
                        'x': df.columns[5:],
                        'y': df.iloc[0, 5:],
                        'type': 'bar'
                    }
                ],
                'layout': {
                    'title': 'Gráfico de Barras'
                }
            }
        )
    ])
    # Adicione mais componentes HTML/Dash de acordo com sua necessidade
  
    
])

@app.callback(Output('graph1', 'figure'), [Input('multi_select_line_chart', 'value')])
def update_line_chart(selected_options):
    traces = []
    
    for option in selected_options:
        traces.append(go.Scatter(x=df_month, y=df[option], mode='lines+markers', name=option))
    
    updated_figure = {'data': traces, 'layout': go.Layout(title='Gráfico de Linha Atualizado')}
    return updated_figure


    
if __name__ == "__main__":
   app.run_server(debug=True)
