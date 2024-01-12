import dash
from dash import html,dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({

    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],

    "Amount": [4, 1, 2, 2, 4, 5],

    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]

})

fig = px.bar(df,x="Fruit",y ="Amount",color = "City")





app.layout = html.Div(id="div1",
    children=[
        html.Label("DropDown"),
        dcc.Dropdown(id="dp-1",options = [{'label':'Rio Grande do Sul','value': 'RS'},
                                         {'label': 'São Paulo','value':'SP'},
                                         {'label': 'Paraná','value': 'PR'}],style={"margin-bottom": "25px"}),

        html.Label("Checklist"),
        dcc.Checklist(id="ch-1",options = [{'label':'Rio Grande do Sul','value': 'RS'},
                                         {'label': 'São Paulo','value':'SP'},
                                         {'label': 'Paraná','value': 'PR'}],style={"margin-bottom": "25px"}),
        html.Label('text Input'),
        dcc.Input(value='Escreva',type='text'),
         html.Label('Slider'),
        dcc.Slider(
                   
                   min = 0,
                   max = 10,
                   marks = {i:'Label {}'.format(i) for i in range (1,6)}, value=5 )                                                                
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

