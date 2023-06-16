# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 16:52:51 2023

@author: khadim
"""
#right

import dash
from dash import Dash, dcc, html, Input, Output , dash_table, State, MATCH
import dash_bootstrap_components as dbc
#import plotly.express as px
#import geopandas as gpd
#import pandas as pd
#from datetime import datetime
from modules.general_statistics import General_Statistics
#import json
#import matplotlib
#matplotlib.use('Agg')

#app2 = dash.Dash(__name__)
#name = name


class CohortDashboard:
    #--------------------general statistics

    def general_statistics(data_gs,lt_id):
                fig1 = General_Statistics.gender(data_gs,lt_id)
                fig2_1,fig2_2 = General_Statistics.distribution_of_biosamples(data_gs,lt_id)
                #fig3 = General_Statistics.venn_diagram()
                #General_Statistics.upsetplot()
                #General_Statistics.venn_diagram()
                res= html.Div([
                        #html.Div([html.Img(src="assets/EMCpilotdataset_2.png",style={'width': '50%', 'text-align': 'center'})],style={'width': '100%', 'text-align': 'center'}), 
                        html.Div([
                        dbc.Row(
                                [
                                dbc.Col([
                                        html.Div('Distribution of samples by Type of biosample (EMC)',style = {'font-size': '30px','font-weight': 'bold','text-align':'center'}),
                                        dcc.Graph(figure=fig2_1)
                                        ],width=4,style = {'text-align':'left'}),
                                dbc.Col([
                                        html.Div('Distribution of samples by Type of biosample (EMBL-EBI)',style = {'font-size': '30px','font-weight': 'bold','text-align':'center'}),
                                        dcc.Graph(figure=fig2_2)
                                        ],width=4,style = {'text-align':'center'}),
                                 dbc.Col([
                                        html.Div([html.Div('Distribution of samples by Gender'),
                                                  #html.Br(),
                                                html.Div( '(Top-level BioSamples)')],style = {'font-size': '30px','font-weight': 'bold','text-align':'center'}),
                                        dcc.Graph(figure=fig1)
                                        ],width=4,style = {'text-align':'right'}),
                                ]),
                        html.Hr(),
                        dbc.Row(
                                [
                                dbc.Col([
                                        html.Div('Venn Diagram between Antibody Profile, Viral Sequence, B-cell, T-cell',style = {'font-size': '30px','font-weight': 'bold','text-align':'center'}),
                                        html.Img(src='assets/venn_1.png',style={'height': '550px'})
                                        ],width=6,style = {'text-align':'left'}),
                                dbc.Col([
                                        html.Div('Upsetplot Diagram between Antibody Profile, Viral Sequence, B-cell, T-cell and the Clinical Data',style = {'font-size': '30px','font-weight': 'bold','text-align':'center'}),
                                        html.Img(src='assets/upsetplot.png',style={'height': '500px'})
                                        ],width=6,style = {'text-align':'center'}),
                                ]),

                        html.Hr(),
                        ###-------------- tab between the heatmap  and the scatter plot 
                        
                        #html.Hr(), 

                        ],style={'width': '100%', 'text-align': 'center'}),
                        
                ])
                return res

        
    def cohortStudy(data,lt_id):
        con = html.Div([
            html.Div([
            html.H1('Erasmus MC COVID-19 cohort-associated connected datasets study',style={'font-weight': 'bold','color':'#193F90','font-size': '65px'}),
             html.Div([html.Div([html.H4('Study aim', style={'font-size': '30px','text-align': 'left', 'font-weight': 'bold', 'margin': '10px 0'}),]
                               , style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'border-bottom': '1px solid black'}),
                                html.Div('''As part of a multidisciplinary consortium (https://recodid.eu/), the study aims at connecting clinical-epidemiological (CE) 
                                data with further datasets from research on many other aspects of SARS-CoV-2. This study includes CE data for a cohort of 151 PCR-confirmed COVID-19
                                individuals from a group of 273 patients who were admitted to the hospital with a respiratory infection or respiratory failure in 2020-2021.''',
                                    style={'text-align': 'justify', 'font-size': '25px', 'margin': '20px 0'})
                    ], style={'margin': '25px', 'text-align': 'center'}),

            ],style={'background-color': '#D0D0CE','border-radius': '20px','width' : '100%','padding': '20px'}),

            html.Div([
                dbc.Row([
                    dbc.Col([
                        ################## Overview
                        html.Div([
                            html.Div([html.H4('Overview', style={'font-size': '30px','text-align': 'left', 'font-weight': 'bold', 'margin': '10px 0'}),]
                               , style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'border-bottom': '1px solid black'}),
                            dbc.Row([
                            dbc.Col([
                                    html.H6('Organisation',style={'font-size': '25px'})
                            ],width=5),
                            dbc.Col([html.P('Erasmus Medical Centre, Rotterdam, Netherlands')
                            ],width=7),
                            ]),
                            dbc.Row([
                            dbc.Col([
                                    html.H6('Website',style={'font-size': '25px'})
                            ],width=5),
                            dbc.Col([html.A('Erasmus MC',href='https://www.erasmusmc.nl/en/research/departments/viroscience')
                            ],width=7),
                            ]),
                            dbc.Row([
                            dbc.Col([
                                    html.H6('Countries',style={'font-size': '25px'})
                            ],width=5),
                            dbc.Col([html.A('Netherlands',href='https://www.google.co.uk/maps/place/Netherlands/@48.734537,15.1942764,5z/data=!4m6!3m5!1s0x47c609c3db87e4bb:0xb3a175ceffbd0a9f!8m2!3d52.132633!4d5.291266!16zL20vMDU5ajI'),
                            ],width=7),
                            ]),
                            dbc.Row([
                            dbc.Col([
                                    html.H6('Location',style={'font-size': '25px'})
                            ],width=5),
                            dbc.Col([html.A('Rotterdam, NL',href='https://www.google.co.uk/maps/place/Rotterdam,+Netherlands/@51.9279653,4.420789,12z/data=!3m1!4b1!4m6!3m5!1s0x47c5b7605f54c47d:0x5229bbac955e4b85!8m2!3d51.9244201!4d4.4777326!16zL20vMDZoZGs'),
                            ],width=7),
                            ])

                            ],style={'background-color': '#D0D0CE','border-radius': '20px','width' : '100%','padding': '20px','margin': '10px','font-size': '25px'}),

                             ######################## General Design
                            html.Div([
                                html.Div([html.H4('General Design', style={'font-size': '30px','text-align': 'left', 'font-weight': 'bold', 'margin': '10px 0'}),]
                               , style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'border-bottom': '1px solid black'}),
                                dbc.Row([
                                dbc.Col([
                                        html.H6('Study design',style={'font-size': '25px'})
                                ],width=5),
                                dbc.Col([html.P('Cohort')
                                ],width=7),
                                ]),
                                dbc.Row([
                                    dbc.Col([
                                            html.H6('Sample size',style={'font-size': '25px'})
                                    ],width=5),
                                    dbc.Col([html.P('273')
                                    ],width=7),
                                ]),
                                dbc.Row([
                                    dbc.Col([
                                            html.H6('Confirmed infections',style={'font-size': '25px'})
                                    ],width=5),
                                    dbc.Col([html.P('151')
                                    ],width=7),
                                ]),
                                dbc.Row([
                                    dbc.Col([
                                            html.H6('Recruitment date',style={'font-size': '25px'})
                                    ],width=5),
                                    dbc.Col([html.P('2020 to 2021')
                                    ],width=7),
                                ]),
                                dbc.Row([
                                    dbc.Col([
                                            html.H6('Follow up schedule',style={'font-size': '25px'})
                                    ],width=5),
                                    dbc.Col([html.P('Until discharged from Erasmus MC; Data further consulted to check survival up to 60 days after inclusion into the study')
                                    ],width=7),
                                ]),

                            ],style={'background-color': '#D0D0CE','border-radius': '20px','width' : '100%','padding': '20px','margin': '10px','font-size': '25px'}),
                            
                        ],width=6,style={'text-align':'left','padding-left': '0%'}),

                    dbc.Col([
                        ##################### Aggregate Data where available
                            html.Div([
                                html.Div([html.H4('Aggregate Data where available', style={'font-size': '30px','text-align': 'center', 'font-weight': 'bold', 'margin': '10px 0'}),]
                               , style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'border-bottom': '1px solid black'}),
                                dbc.Row([
                                        dbc.Col([
                                                html.H6('Age range ',style={'font-size': '25px'})
                                        ],width=3),
                                        dbc.Col([html.P('20 - 78')
                                        ],width=9),
                                    ]),
                                dbc.Row([
                                        dbc.Col([
                                                html.H6('Comorbidities ',style={'font-size': '25px'})
                                        ],width=3),
                                        dbc.Col([html.P('Chronic cardiac disease (not hypertension), Hypertension, Chronic pulmonary disease (not asthma), Asthma (physician diagnosed), Chronic kidney disease, Obesity (as defined by clinical staff), Moderate or severe liver disease, Mild liver disease, Chronic neurological disorder, Malignant neoplasm, Chronic hematologic disease, Rheumatologic disorder, Malnutrition, Smoking')
                                        ],width=9),
                                    ]),
                                 dbc.Row([
                                        dbc.Col([
                                                html.H6('Medication ',style={'font-size': '25px'})
                                        ],width=3),
                                        dbc.Col([html.P('Antiviral or COVID-19 targeted agent (Ribavirin, Lopinavir/Ritonvir, Remdesivir (Veklury), Neuraminidase inhibitors, Interferon alpha, Interferon beta, Chloroquine/hydroxychloroquine), Antibiotic, Heparin, Antifungal agent')
                                        ],width=9),
                                    ]),
                                dbc.Row([
                                        dbc.Col([
                                                html.H6('Treatment ',style={'font-size': '25px'})
                                        ],width=3),
                                        dbc.Col([html.P('Any Oxygen therapy, Non-invasive ventilation, Invasive ventilation, Prone positioning, Inhaled Nitric Oxide, Tracheostomy inserted, Extracorporeal support (ECMO), Renal replacement therapy (RRT) or dialysis, Inotropes / vasopressors, ICU or High Dependency Unit admission')
                                        ],width=9),
                                    ]),
                                dbc.Row([
                                        dbc.Col([
                                                html.H6('Outcome ',style={'font-size': '25px'})
                                        ],width=3),
                                        dbc.Col([html.P('Discharged alive,Transfer to other facility,Death')
                                        ],width=9),
                                    ]),
                            ],style={'background-color': '#D0D0CE','border-radius': '20px','width' : '100%','padding': '20px','margin': '10px','font-size': '25px'}),   
                        ],width=6,style={'text-align':'left','padding-left': '0%'}),
            ]),]),
            
        html.Hr(),
        #   general statistics 

        CohortDashboard.general_statistics(data,lt_id),

        #html.Hr(),


        ], style={'margin-left':'100px','margin-top': '50px','margin-right':'100px','text-align':'center'})
        return con






