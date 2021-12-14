"""
SCRIPT FOR ELEMENTS ON A DASH 
AUTHOR: C GARVEY
DATE: 13/12/2021

STATUS: WIP

"""
#-----------------------------------------
# Import modules

import matplotlib.pyplot as plt
import numpy as np
import math
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table as dt
import plotly.express as px
import pandas as pd
from plotly.tools import mpl_to_plotly
from io import BytesIO
import base64



#-----------------------------------------
#----------Text input element --supply the Slope file to analyse ---
#-----------------------------------------
# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H2("Slope output file path (.json)"),
#     html.Div([
#         "Input: ",
#         dcc.Input(id='input', value='<empty>', type='text')
#     ]),
#     html.Br(),
#     html.Div(id='requested_file_path'),

# ])

# # move this above the slope results callback
# # slope results to copy the Input of the Output below.
# @app.callback(
#     Output(component_id='requested_file_path', component_property='children'),
#     Input(component_id='input', component_property='value')
# )
# def update_file_path(requested_file_path):
#     return 'Output: {}'.format(requested_file_path)


# if __name__ == '__main__':
#     app.run_server(debug=True)





#-----------------------------------------
#----Graph of Slope Results with Slider---
#-----------------------------------------

#****************************************************
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64
def fig_to_uri(in_fig, close_all=True, **save_args):
    # type: (plt.Figure) -> str
    """
    Save a figure as a URI
    :param in_fig:
    :return:
    """
    out_img = BytesIO()
    in_fig.savefig(out_img, format='png', **save_args)
    if close_all:
        in_fig.clf()
        plt.close('all')
    out_img.seek(0)  # rewind file
    encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
    return "data:image/png;base64,{}".format(encoded)
#****************************************************

import sys
sys.path.append('C:/Users/christian.garvey/OneDrive - Arup/01 Documents/01-07 Digital/Python/ukimea-automation-training-2022/Individual_project/individual_project_cgarvey/json/')
import extract_data_from_json
df = extract_data_from_json.slope_output_df

factor_min = 0 #math.floor(df['Factor'].min())
factor_max = math.ceil(df['Factor'].max())

app = dash.Dash(__name__)

#from functions_dash import fig_to_uri

#***********LAYOUT*************************

app.layout = html.Div([
    #dcc.Graph(id='mpl-graph-with-slider', figure=plotly_fig),
    html.Div([html.Img(id = 'mpl-graph', src = '')]),
    dcc.Input(id='factor_input_lwr', value=factor_max, type="number"),
    dcc.Input(id='factor_input_uppr', value=factor_max, type="number")
])


#***********PLOTTING*************************
### HOW TO OVERLAY THE GRAPHIC WITH STRATUM GEOMETRY DATA??
#df = extract_data_from_json.stratum_geometry_df

### callback for requested json file --> output: json file path 
    # f = dir + "\\" + file_name
    # fo = open(f)
    # # Read data from file
    # data = json.loads(fo.read())

@app.callback(
    # output(component_id = <id>, component_type = <data type>)
    Output('mpl-graph', 'src'),
    [Input('factor_input_lwr', 'value'), 
    Input('factor_input_uppr', 'value')])
def update_figure(input_lwr_value, input_uppr_value):
    filtered_df = df[(df["Factor"] >= input_lwr_value) & (df["Factor"] <= input_uppr_value)]

#***********MATPLOTLIB SETUP*************************
    #centre points are at Slope Results['X'] and ['Y'] 
    centre_points_x = filtered_df["X"]
    centre_points_y = filtered_df["Y"]
    
    fig, ax = plt.subplots()#figsize = (50,100))
    ax.set_xlim([-20,70])
    ax.set_ylim([-5,50])
    ax.scatter(centre_points_x, y=centre_points_y)
    ax.set_title("Showing slip circles with a Factor between: \n" + str(input_lwr_value) + " and " + str(input_uppr_value))
    
    
    # fig = plt.patches.Arc() 
    #     data=[go.matplotlib [0,1,2,3,4])


#********************************************************
    out_url = fig_to_uri(fig)
    #fig.update_layout(transition_duration=500)
    return out_url

if __name__ == '__main__':
    app.run_server(debug=True)