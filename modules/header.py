import dash
from dash import Dash, dcc, html, Input, Output , dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import geopandas as gpd
import pandas as pd
from datetime import datetime


class Header :
    def __init__(self):
        init = 0 
    def header():
        header = html.Div([
            html.Div([
            dbc.Row(
            [
                
                dbc.Col([
                    html.A([html.Img(src="assets/logo_biosamples.png",style={'width': '80px', 'text-align': 'right', 'display': 'inline'}),
                             html.P('BioSamples', style={'display': 'inline', 'margin-left': '10px','color':'#ffffff'})], href='https://www.ebi.ac.uk/biosamples/', style={'display': 'inline-block'})
                    ],width=8, style={'display':'inline'}),
                dbc.Col([
                    html.A([html.Img(src="assets/ENA_Logo_notagline.png",style={'width' : '600px','text-align': 'left'})], href = 'https://www.ebi.ac.uk/ena/browser/home') 
                    ],width=4)
            ])
        ,
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Home", active=True, href="https://www.ebi.ac.uk/biosamples/" ,style={'color':'#ffffff'})),
                dbc.NavItem(dbc.NavLink("Search", active=True, href="https://www.ebi.ac.uk/biosamples/samples" ,style={'color':'#ffffff'})),
                dbc.NavItem(dbc.NavLink("Upload", active=True, href="https://www.ebi.ac.uk/biosamples/uploadLogin" ,style={'color':'#ffffff'})),
                dbc.NavItem(dbc.NavLink("Graph Search", active=True, href="https://www.ebi.ac.uk/biosamples/graph/search" ,style={'color':'#ffffff'})),
                dbc.NavItem(dbc.NavLink("Submit", active=True, href="https://www.ebi.ac.uk/biosamples/submit" ,style={'color':'#ffffff'})),
                dbc.NavItem(dbc.NavLink("Documentation", active=True, href="https://www.ebi.ac.uk/biosamples/docs" ,style={'color':'#ffffff'})),
                dbc.NavItem(dbc.NavLink("About", active=True, href="https://www.ebi.ac.uk/biosamples/about" ,style={'color':'#ffffff'})),
                dbc.NavItem(dbc.NavLink("Cohort Biosamples", active=True, href="#",style={'color':'red'})),
            ]
        ,style={'font-size': '23px','width' : '100%','margin-left': '30%'})
        ])

        ],style={'font-size': '80px' ,'font-weight': 'bold', 'width' : '100%','background-color': '#007B53','text-align': 'center'})
        
        return header






