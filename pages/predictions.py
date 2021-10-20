from joblib import load
model = load('assets/pipeline.joblib')

# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [   dcc.Markdown('## Predict the Species of Penguin!'),
        dcc.Markdown('#### Island'),
        dcc.Dropdown(
            id='island',
            options = [
            {'label': 'Biscoe', 'value': 'Biscoe'},
            {'label': 'Torgersen', 'value': 'Torgersen'},
            {'label': 'Dream', 'value': 'Dream'}
            ],
            value='Biscoe'),
        dcc.Markdown('#### Bill Length (mm)'),
        dcc.Slider(
            id='bill_length', 
            min=32, 
            max=60, 
            step=1, 
            value=40, 
            marks={n: str(n) for n in range(32,61,3)}
            ),
        dcc.Markdown('#### Bill Depth (mm)'),
        dcc.Slider(
            id='bill_depth', 
            min=13, 
            max=22, 
            step=1, 
            value=15, 
            marks={n: str(n) for n in range(13, 23, 1)}
            ),
    ],
    md=6,
)

column2 = dbc.Col(
    [
        dcc.Markdown('#### Flipper Length (mm)'),
        dcc.Slider(
            id='flipper_length', 
            min=170, 
            max=230, 
            step=5, 
            value=200, 
            marks={n: str(n) for n in range(170, 240, 10)}
            ),
        dcc.Markdown('#### Penguin Mass (g)'),
        dcc.Slider(
            id='mass', 
            min=2700, 
            max=6300, 
            step=100, 
            value=4200, 
            marks={n: str(n) for n in range(2700, 6300, 500)}
            ),
        dcc.Markdown('#### Sex'),
        dcc.Dropdown(
            id='sex',
            options = [
            {'label': 'Male', 'value': 'Male'},
            {'label': 'Female', 'value': 'Female'},
            ],
            value='Female'),
        html.H2('Penguin Species'),
        html.Div(id='prediction-content', className='lead')
    ]
)

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'), 
    [Input('island', 'value'), Input('bill_length', 'value'), Input('bill_depth', 'value'), Input('flipper_length', 'value'), Input('mass', 'value'), Input('sex', 'value')]
)
def predict(island, bill_length, bill_depth, flipper_length, mass, sex):
    # print(island, bill_length, bill_depth, flipper_length, mass, sex)
    
    df = pd.DataFrame(columns=['island', 'bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g', 'sex'],
       data=[[island, bill_length, bill_depth, flipper_length, mass, sex]])

    y_pred = model.predict(df)

    # print(y_pred)

    return y_pred


layout = dbc.Row([column1, column2])










