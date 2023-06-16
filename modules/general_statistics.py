import dash
from dash import Dash, dcc, html, Input, Output , dash_table
#import dash_bootstrap_components as dbc
#import plotly.express as px
#import geopandas as gpd
import pandas as pd
#from datetime import datetime
#from modules.header import Header
import plotly.graph_objects as go
import json
#from upsetplot import from_contents , UpSet
#from venn import venn
#import matplotlib.pyplot as plt
#import os


class General_Statistics:
    xls = pd.ExcelFile('assets/data/ReCoDID_EMCpilot_sampleIDs.xlsx')
    l  = xls.sheet_names
    f = pd.read_excel(xls, l[0],header=None)
    EGA = ' '.join([str(i) for i in list(f[0])])
    B_cell = ' '.join([str(i) for i in [list(f[2]),list(f[3]),list(f[4]),list(f[5])]])
    T_cell = ' '.join([str(i) for i in [list(f[6]),list(f[7]),list(f[8]),list(f[9]),list(f[10])]])
    Antibody_profile = ' '.join([str(i) for i in [list(f[11]),list(f[12]),list(f[13]),list(f[14]),list(f[15]),list(f[16])]])
    ENA_SARS_CoV_2_records = ' '.join([str(i) for i in [list(f[17]),list(f[18]),list(f[19]),list(f[20])]])

    def distribution_of_biosamples(data,lt_id):
        ega = 0
        bcell = 0 
        tcell = 0 
        antibody = 0 
        ena = 0 
        non = 0 
        lt_id_str = ' '.join(lt_id)
        for item in data:
            #if lt_id_str.find(str(item['accession'])) != -1 :
            if General_Statistics.EGA.find(str(item["accession"] )) != -1 :
                ega += 1
            elif General_Statistics.B_cell.find(str(item["accession"] )) != -1 :
                bcell += 1
            elif General_Statistics.T_cell.find(str(item["accession"] )) != -1 :
                tcell +=1 
            elif General_Statistics.Antibody_profile.find(str(item["accession"] )) != -1 :
                antibody +=1
            elif General_Statistics.ENA_SARS_CoV_2_records.find(str(item["accession"] )) != -1 :
                ena +=1
            else : 
                non += 1
        val1 =[ega,bcell,tcell,antibody,ena,non]
        pull_val1 = []
        for i in val1:
            if int(i)/sum(val1) > 0.01:
                pull_val1.append(0)
            else:
                pull_val1.append(0.2)
        fig1 = go.Figure(data=[go.Pie(labels=['EGA','B-cell data','T-cell data','Antibody profile','ENA SARS-CoV-2','None'], values=val1, pull=pull_val1)])
        fig1.update_layout(
            autosize=False,
            width=620,
            height=500,
            legend_title_text='',
            legend=dict(font=dict(size=16), x=1, y=1, orientation='v')
            )
        
        val2 =[ega,bcell,tcell,antibody,ena,non]
        pull_val2 = []
        for i in val2:
            if int(i)/sum(val2) > 0.01:
                pull_val2.append(0)
            else:
                pull_val2.append(0.2)
        fig2 = go.Figure(data=[go.Pie(labels=['EGA','B-cell data','BioStudies','Array-Express','ENA','None'], values=val2, pull=pull_val2)])
        fig2.update_layout(
            autosize=False,
            width=620,
            height=500,
            legend_title_text='',
            legend=dict(font=dict(size=16), x=1, y=1, orientation='v')
            )

        return fig1,fig2
            
    def gender(data,lt_id):
        m = 0 
        f = 0 
        n = 0
        lt_id_str = ' '.join(lt_id)
        for item in data:
            if lt_id_str.find(str(item['accession'])) != -1 :
                if ('gender' in item['characteristics']) and ('text' in item['characteristics']['gender'][0]):
                    if str(item['characteristics']['gender'][0]['text']).find('female') != -1 :
                        f +=1
                    elif str(item['characteristics']['gender'][0]['text']).find('male') != -1 :
                        m += 1
                    else:
                        n+=1
                else:
                    n+=1
        val =[m,f,n]
        pull_val = []
        for i in val:
            if int(i)/sum(val) > 0.01:
                pull_val.append(0)
            else:
                pull_val.append(0.2)
        fig = go.Figure(data=[go.Pie(labels=['Male','Female','None'], values=val, pull=pull_val)])
        fig.update_layout(
            autosize=False,
            width=470,
            height=500,
            legend_title_text='',
            legend=dict(font=dict(size=16), x=1, y=1, orientation='v')
            )
        return fig 
    
    '''
    def venn_diagram():
        EMCpilot = {
            "Antibody Profile": {1, 2, 3, 4, 5, 7, 11, 12, 13, 14, 15, 16, 17, 19, 24, 25, 26, 27, 29, 32, 33, 34, 40, 42, 43, 44, 48, 52, 54, 55, 56, 59, 60, 61, 67, 69, 71, 73, 74, 76},
            "Viral Sequence": {1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 39, 40, 41, 42, 43, 44, 45, 51, 54, 55, 56, 57, 58, 59, 60, 61, 62, 65, 66, 67, 68, 71, 72, 73, 74, 77, 82, 87, 93, 99, 135, 141},
            "B-cell": {4, 5, 7, 11, 12, 13, 14, 21, 22, 23, 28, 30, 31, 34, 36, 37, 46},
            "T-cell": {1, 2, 3, 4, 5, 7, 11, 12, 13, 14, 18, 20, 21, 22, 23, 28, 30, 31, 34, 36, 37, 46, 47, 48, 50, 51, 53, 55}
        }
        try :
            venn(EMCpilot)
        except:
            print('install : $ pip install venn or use from matplotlib_venn import venn3 ')
        #return venn(EMCpilot)
        #if os.path.exists('assets/venn_1.png'):
        #    os.remove('assets/venn_1.png')
        plt.savefig('assets/venn_1.png')
    
    def upsetplot ():
        Viral_Sequence	= [1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 39, 40, 41, 42, 43, 44, 45, 51, 54, 55, 56, 57, 58, 59, 60, 61, 62, 65, 66, 67, 68, 71, 72, 73, 74, 77, 82, 87, 93, 99, 135, 141]
        Antibody_Profile = [1, 2, 3, 4, 5, 7, 11, 12, 13, 14, 15, 16, 17, 19, 24, 25, 26, 27, 29, 32, 33, 34, 40, 42, 43, 44, 48, 52, 54, 55, 56, 59, 60, 61, 67, 69, 71, 73, 74, 76]
        Bcell_Data =	[4, 5, 7, 11, 12, 13, 14, 21, 22, 23, 28, 30, 31, 34, 36, 37, 46]
        Tcell_Data	= [1, 2, 3, 4, 5, 7, 11, 12, 13, 14, 18, 20, 21, 22, 23, 28, 30, 31, 34, 36, 37, 46, 47, 48, 50, 51, 53, 55]
        Clinical_Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 65, 66, 67, 68, 69, 71, 72, 73, 74, 76, 77, 82, 87, 93, 99, 135, 141]
        EMCpilot = from_contents({'Viral Sequence': Viral_Sequence, 'Antibody Profile': Antibody_Profile, 'B-cell Data': Bcell_Data, 'T-cell Data': Tcell_Data, 'Clinical Data': Clinical_Data})
        try:
            ax_dict = UpSet(EMCpilot, subset_size='count', show_counts=True, sort_by='cardinality').plot()
        except:
            print('install : $ pip install upsetplot ')
        #if os.path.exists('assets/upsetplot.png'):
        #    os.remove('assets/upsetplot.png')
        plt.savefig('assets/upsetplot.png')
    '''

    def heatmap(df):
        #df = pd.read_excel('assets/data/ReCoDID_EMCpilot_sampleIDs.xlsx', header=3, index_col= 'top-level accession', usecols=[col for col in range(22, 30) if col != 23])
        #df = df.dropna(axis=0, how='all')
        data = [
            go.Heatmap(
                z=df.values,
                x=df.columns,
                y=df.index,
                colorscale='RdYlGn',
            )
        ]
        #height = int(len(df.index)*3000/151) + 1
        #if height < 100 : 
        #    height = 500
        #print (height)
        layout = go.Layout(
            yaxis=dict(title='Top-level accession',autorange='reversed'),
            xaxis=dict(title='number of data points per type',side='top'),
            #font=dict(size=16),
            height=3000,
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='right',
                x=1,
                traceorder='reversed',
                title='Legend',
                font=dict(size=10)
            )
        )

        # Create the figure
        fig = go.Figure(data=data, layout=layout)
        return fig 
    
    def scatter_heatmap(df): # df comme input 
        layout = go.Layout(
            yaxis=dict(title='Top-level accession',autorange='reversed'),
            xaxis=dict(title='number of data points per type',side='top'),
            #font=dict(size=16),
            height=6000
         )
        fig = go.Figure( layout=layout)



        for i in range(1, len(df.columns)+1):
            x = []
            y = []
            t = []
            for j in range(len(df)):
                x.append(i)
                y.append(j)
                t.append(int(df.iloc[j, i-1])*10)
            fig.add_trace(go.Scatter(
                x=x, y=y, mode='markers', marker=dict(size=t, color='blue'),
                text=['number of data points: '+str(int(e/10))  for e in t], textposition='middle center',
                showlegend=False
            ))

        fig.update_xaxes(tickmode='array', tickvals=list(range(1, len(df.columns)+1)), ticktext=list(df.columns)[::1], showticklabels=True, side='top')
        fig.update_yaxes(tickmode='array', tickvals=list(range(len(df.index))), ticktext=list(df.index)[::1], showticklabels=True,range=[0, len(df.index)])

        return fig


    def Relationships(data, lt_id):
        Source = []
        Type = []
        Target = []
        lt_id_str = ' '.join(lt_id)
        for item in data:
            if lt_id_str.find(str(item['accession'])) != -1:
                if 'relationships' in item:
                    for items in item['relationships']:
                        Source.append(f"[{items['source']}](https://www.ebi.ac.uk/biosamples/samples/{items['source']})")
                        Type.append(items['type'])
                        Target.append(f"[{items['target']}](https://www.ebi.ac.uk/biosamples/samples/{items['target']})")
                else:
                    Source.append(' - ')
                    Type.append(' - ')
                    Target.append(f"[{item['accession']}](https://www.ebi.ac.uk/biosamples/samples/{item['accession']})")
        dta = pd.DataFrame({'Source': Source, 'Type': Type, 'Target': Target})
       

        # Generate alternating row colors based on target IDs
        target_ids = dta['Target'].unique()
        target_ids_odd = [target_ids[i] for i in range(len(target_ids)) if i % 2 == 0]
        row_colors= []
        p = 0
        for i in range(len(dta['Target'])):
            if p < 58:
                p+= 1
            else:
                p = 0
            if dta['Target'][i] in target_ids_odd:
                row_colors.append({'if': {'filter_query': f"{{Target}} = '{dta['Target'][i]}'"}, 'backgroundColor': '#D0D0CE'})
            else: 
                row_colors.append({'if': {'filter_query': f"{{Target}} = '{dta['Target'][i]}'"}, 'backgroundColor': 'white'} )
        #row_colors = [{'if': {'row_index': i}, 'backgroundColor': '#D0D0CE'} if dta['Target'].iloc[i] in target_ids_odd else {'if': {'row_index': i}, 'backgroundColor': 'white'} for i in range(len(dta))] 
        table_Relationships = html.Div([dash_table.DataTable(
            id='table',
            columns=[
                {'name': 'Source', 'id': 'Source', 'type': 'text', 'presentation': 'markdown'},
                {'name': 'Type', 'id': 'Type', 'type': 'text', 'presentation': 'markdown'},
                {'name': 'Target', 'id': 'Target', 'type': 'text', 'presentation': 'markdown'}
            ],
            data=dta.to_dict('records'),
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            row_deletable=False,
            selected_rows=[],
            page_action="native",
            page_current=0,
            page_size=58,
            style_data_conditional=row_colors,  # Apply alternating row colors
            style_cell={'textAlign': 'center'},
            style_header={'backgroundColor': '#D0D0CE'},
        )], style={
        'textAlign': 'center',
        'font-size': '20px'
            })

        res = html.Div([
            table_Relationships,
        ])

        return res



