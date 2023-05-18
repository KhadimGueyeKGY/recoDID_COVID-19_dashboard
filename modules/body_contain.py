import dash
from dash import Dash, dcc, html, Input, Output , dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px
import geopandas as gpd
import pandas as pd
from datetime import datetime
from modules.header import Header
import json


class Contain :
    #--------------------------
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
    #------------------

    def generate_table(item):
        rows = []
        if item['accession']:
            rows.append( html.Tr([html.Th(html.A(item["accession"] , href='https://www.ebi.ac.uk/biosamples/samples/'+str(item["accession"])),style={'width': '30%'}), html.Th(item['name'],style={'width': '70%'})], style={'font-size': '40px'}))
        else:
            rows.append(None)
        if ('collection date' in item['characteristics']) and ('text' in item['characteristics']['collection date'][0]):
            rows.append(html.Tr([html.Td( 'Collection date:',style={'width': '30%'}), html.Td(item['characteristics']['collection date'][0]['text'],style={'width': '70%'})] , style={'font-size': '20px'}))
        else : 
            rows.append(None) 
        if item['submitted']:
            rows.append(html.Tr([html.Td( 'Submitted on:',style={'width': '30%'}), html.Td(item['submitted'],style={'width': '70%'})], style={'font-size': '20px'}))
        else:
           rows.append(None)
        if item['release']:
            rows.append(html.Tr([html.Td( 'Release on:',style={'width': '30%'}), html.Td(item['release'],style={'width': '70%'})], style={'font-size': '20px'}))
        else:
            rows.append(None) 
        if ('ENA first public' in item['characteristics']) and ('text' in item['characteristics']['ENA first public'][0]):
            rows.append(html.Tr([html.Td( 'ENA first public:',style={'width': '30%'}), html.Td(item['characteristics']['ENA first public'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None) 
        if ('INSDC first public' in item['characteristics']) and ('text' in item['characteristics']['INSDC first public'][0]):
            rows.append(html.Tr([html.Td( 'INSDC first public:',style={'width': '30%'}), html.Td(item['characteristics']['INSDC first public'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('checklist' in item['characteristics']) and ('text' in item['characteristics']['checklist'][0]):
            rows.append(html.Tr([html.Td( 'CHECKLIST:',style={'width': '30%'}), html.Td(item['characteristics']['checklist'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('collection time point' in item['characteristics']) and ('text' in item['characteristics']['collection time point'][0]):
            rows.append(html.Tr([html.Td( 'Collection time point:',style={'width': '30%'}), html.Td(item['characteristics']['collection time point'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None) 
        if ('ENA-CHECKLIST' in item['characteristics']) and ('text' in item['characteristics']['ENA-CHECKLIST'][0]):
            rows.append(html.Tr([html.Td( 'ENA CHECKLIST:',style={'width': '30%'}), html.Td(item['characteristics']['ENA-CHECKLIST'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('External Id' in item['characteristics']) and ('text' in item['characteristics']['External Id'][0]):
            rows.append(html.Tr([html.Td( 'External Link:',style={'width': '30%'}), html.Td(item['characteristics']['External Id'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('GISAID Accession ID' in item['characteristics']) and ('text' in item['characteristics']['GISAID Accession ID'][0]):
            rows.append(html.Tr([html.Td( 'GISAID Accession ID:',style={'width': '30%'}), html.Td(item['characteristics']['GISAID Accession ID'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('SRA accession' in item['characteristics']) and ('text' in item['characteristics']['SRA accession'][0]):
            rows.append(html.Tr([html.Td( 'SRA accession:',style={'width': '30%'}), html.Td(item['characteristics']['SRA accession'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('gender' in item['characteristics']) and ('text' in item['characteristics']['gender'][0]):
            rows.append(html.Tr([html.Td( 'Gender:',style={'width': '30%'}), html.Td(item['characteristics']['gender'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('disease' in item['characteristics']) and ('ontologyTerms' in item['characteristics']['disease'][0]):
            rows.append(html.Tr([html.Td( 'Disease:',style={'width': '30%'}), html.Td(html.A(item['characteristics']['disease'][0]['text'], href=item['characteristics']['disease'][0]['ontologyTerms'][0]),style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('taxId' in item):
            rows.append(html.Tr([html.Td( 'Taxonomy ID:',style={'width': '30%'}), html.Td(html.A(item['taxId'], href='https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id='+str(item['taxId'])),style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('organism' in item['characteristics']):
             rows.append(html.Tr([html.Td( 'Organism:',style={'width': '30%'}), html.Td(html.A(item['characteristics']["organism"][0]['text'], href=item['characteristics']['organism'][0]['ontologyTerms'][0]),style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('project name' in item['characteristics']):
            rows.append(html.Tr([html.Td( 'Project name:',style={'width': '30%'}), html.Td(item['characteristics']['project name'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('sample title' in item['characteristics']):
            rows.append(html.Tr([html.Td( 'Sample title:',style={'width': '30%'}), html.Td(item['characteristics']['sample title'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('sample soure name' in item['characteristics']):
             rows.append(html.Tr([html.Td( 'Sample soure name:',style={'width': '30%'}), html.Td(html.A(item['characteristics']["sample soure name"][0]['text'], href=item['characteristics']['sample soure name'][0]['ontologyTerms'][0]),style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('sample description' in item['characteristics']):
            rows.append(html.Tr([html.Td( 'Description:',style={'width': '30%'}), html.Td(item['characteristics']['sample description'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('organization' in item['characteristics']) and ('Name' in item['characteristics']['organization'][0]):
            rows.append(html.Tr([html.Td( 'Organization:',style={'width': '30%'}), html.Td(item['characteristics']['organization'][0]['Name'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('INSDC center name' in item['characteristics']) and ('text' in item['characteristics']['INSDC center name'][0]):
            rows.append(html.Tr([html.Td( 'INSDC center name:',style={'width': '30%'}), html.Td(item['characteristics']['INSDC center name'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('collector name' in item['characteristics']) and ('text' in item['characteristics']['collector name'][0]):
            rows.append(html.Tr([html.Td( 'Collector name:',style={'width': '30%'}), html.Td(item['characteristics']['collector name'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        if ('geographic location (country and/or sea)' in item['characteristics']) and ('text' in item['characteristics']['geographic location (country and/or sea)'][0]):
            rows.append(html.Tr([html.Td( 'Geographic location (country and/or sea):',style={'width': '30%'}), html.Td(item['characteristics']['geographic location (country and/or sea)'][0]['text'],style={'width': '70%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        return dbc.Table(children=[row for row in rows if row],style={'width': '100%','text-align':'left','margin-left': '20px','margin-right': '20px'})

    def relationships(item):
        rows = []
        rows.append( html.Tr([html.Th('Source',style={'width': '35%'}),html.Th('Type',style={'width': '30%'}), html.Th('Target',style={'width': '35%'})], style={'font-size': '20px'}))
        if ('relationships' in item):
             for items in item['relationships']:
                 rows.append( html.Tr([html.Td(html.A(items['source'],href='https://www.ebi.ac.uk/biosamples/samples/'+str(items['source'])),style={'width': '35%'}),html.Td(items['type'],style={'width': '30%'}), html.Td(html.A(items['target'],href='https://www.ebi.ac.uk/biosamples/samples/'+str(items['target'])),style={'width': '35%'})], style={'font-size': '20px'}))
        else : 
            rows.append(None)
        return dbc.Table(children=[row for row in rows if row],style={'width': '100%','text-align':'center'})
    
    def contain (item):
        contain= html.Div([
                                html.Div([
                                html.H1('Relationships',style={'text-align':'center','margin-right':'7px','font-size': '40px','font-weight': 'bold'}),
                                html.Hr(style={'border': '1px solid aqua', 'background-color': 'aqua'}),
                                Contain.relationships(item)
                                ],style={'width': '30%','float':'right'}),
                                
                                html.Div([
                                    Contain.generate_table(item)
                                ],style={'width': '70%'})
                            
                            ],style={'width': '100%'})
        return contain
    
