# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            # Big Title

            ## Smaller Title

            ### Even Smaller Title

            Paragraph text looks like this.

            [This is a link to Lambda School](http://lambdaschool.com)
            """
        ),
        dcc.Link(dbc.Button('Try it out!', color='primary'), href='/predictions')
    ],
    md=4,
)

penguins = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
fig = px.scatter(penguins, x="bill_depth_mm", y="bill_length_mm", color="species",
           hover_name="species", size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

# column2 = dbc.Col(
#     [
#         html.Img(src='assets/scatterplot_screenshot.png', width=600)
#     ],
#     md=8,
# )


layout = dbc.Row([column1, column2])