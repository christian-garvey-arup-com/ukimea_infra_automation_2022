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
import plotly.graph_objects as go
import pandas as pd
# from plotly.tools import mpl_to_plotly
# from io import BytesIO
# import base64



#-----------------------------------------
#----------Text input element --supply the Slope file to analyse ---
#-----------------------------------------
# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H2("Slope output file path (.json)"),
#     html.Div([
#         "Input: ",
#         dcc.Input(id='input', value='paste file name here...', type='text')
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

#****************************************************

import sys
sys.path.append('C:/Users/christian.garvey/OneDrive - Arup/01 Documents/01-07 Digital/Python/ukimea-automation-training-2022/Individual_project/individual_project_cgarvey/json/')
import extract_data_from_json
#from functions_json import slope_results_df
from functions_json import get_strata_list #, get_hex_colour
from functions_json import get_json_data, rgbint_to_hex
from functions_json import extract_json_data
df = extract_data_from_json.slope_output_df
stratum_geometry_df =extract_data_from_json.stratum_geometry_df
material_data_df = extract_data_from_json.material_data_df
slope_output_df = extract_data_from_json.slope_output_df
stratum_geometry_rgb_df = extract_data_from_json.stratum_geometry_rgb_df

factor_min = 0 #math.floor(df['Factor'].min())
factor_max = math.ceil(df['Factor'].max())
arc_x_list = []
arc_y_list = []

app = dash.Dash(__name__)

#***********LAYOUT*************************

app.layout = html.Div([
    #Text input element --supply the Slope file to analyse ---
    html.H2("Slope output file path (.json)"),
    html.Div([
        "Input: ",
        dcc.Input(id='input', value='Slope01_output.json', type='text')
    ]),
    html.Br(),
    html.Div(id='requested_file_path'),

    dcc.Graph(id='slope_results_with_slider'),
    #html.Div([html.Img(id = 'mpl-graph', src = '')]),
    dcc.Input(id='factor_input_lwr', value=factor_min, type="number"),
    dcc.Input(id='factor_input_uppr', value=factor_max, type="number")
])

#***********PLOTTING*************************

@app.callback(
    Output(component_id='requested_file_path', component_property='children'),
    Input(component_id='input', component_property='value')
)
def update_file_path(requested_file_path):
    file_name = requested_file_path 
    dir = r"C:\Users\christian.garvey\OneDrive - Arup\01 Documents\01-07 Digital\Python\ukimea-automation-training-2022\Individual_project\individual_project_cgarvey"
    data = (get_json_data(file_name, dir))
    
    #Dive into function to change variables.

    global stratum_geometry_df
    stratum_geometry_df = extract_json_data(data)[0]
    global material_data_df
    material_data_df = extract_json_data(data)[1]
    slope_output_df = extract_json_data(data)[2]
    global df 
    df = slope_output_df
    global stratum_geometry_rgb_df
    stratum_geometry_rgb_df = pd.merge(stratum_geometry_df, material_data_df[["Name", "RGBStratum"]], on="Name", how="left")
    stratum_geometry_rgb_df["hex_code"] = [rgbint_to_hex(i) for i in stratum_geometry_rgb_df["RGBStratum"]]
    #print(stratum_geometry_rgb_df)

    return 'Output: {}'.format(requested_file_path)



@app.callback(
    # output(component_id = <id>, component_type = <data type>)
    Output('slope_results_with_slider', 'figure'),
    [Input('factor_input_lwr', 'value'), 
    Input('factor_input_uppr', 'value')])
def update_figure(input_lwr_value, input_uppr_value):
    arc_x_list = []
    arc_y_list = []
    filtered_df = df[(df["Factor"] >= input_lwr_value) & (df["Factor"] <= input_uppr_value)]
    print(len(filtered_df))
    print(filtered_df.head(n=20))
    filtered_df = filtered_df.reset_index()#inplace=True) #drop=True, 
    print(filtered_df.head(n=20))
    #centre points are at Slope Results['X'] and ['Y'] 
    centre_points_x = filtered_df["X"]
    centre_points_y = filtered_df["Y"]

#***********MATPLOTLIB SETUP*************************    
    # fig, ax = plt.subplots()#figsize = (50,100))
    # ax.set_xlim([-20,70])
    # ax.set_ylim([-5,50])
    # ax.scatter(centre_points_x, y=centre_points_y)
    # ax.set_title("Showing slip circles with a Factor between: \n" + str(input_lwr_value) + " and " + str(input_uppr_value))
    # out_url = fig_to_uri(fig)
#     return out_url

#***********PLOTLY GO SETUP --> THINK ABOUT CHANGING THIS TO PX*************************    
    #Geometry
    ## IMPROVE --> EXPLODE THE DF TO EXPOSE XYZ INSTEAD OF USING FN
    ## MAKE THIS CLEVERER SO LOOPS THROUGH ALL GEOMETRY IN A DATAFRAM
    clay_x = get_strata_list(stratum_geometry_rgb_df, "Clay","X")
    clay_y = get_strata_list(stratum_geometry_rgb_df, "Clay","Y")
    sand_x = get_strata_list(stratum_geometry_rgb_df, "Sand","X")
    sand_y = get_strata_list(stratum_geometry_rgb_df, "Sand","Y")
    
    
    #Slip circle arcs
    start_x = filtered_df["arc_start_x"]
    start_y = filtered_df["arc_start_y"]
    end_x = filtered_df["arc_end_x"]
    end_y = filtered_df["arc_end_y"]

 
    # ### Calculate points along an arc for each start xy and end xy.
    from functions_dash import arc_points
    for i in range(0,len(start_x)):     # len start_x is arbitrary
        x_pts = arc_points(start_x[i],start_y[i],end_x[i],end_y[i],0.5)[0]
        arc_x_list.append(x_pts)
        y_pts = arc_points(start_x[i],start_y[i],end_x[i],end_y[i],0.5)[1]
        arc_y_list.append(y_pts)

    print("No of arcs shown: ", len(arc_y_list), len(arc_x_list))
    arc_data = {"arc_x": arc_x_list, "arc_y": arc_y_list}
    arc_df = pd.DataFrame(arc_data)  



    #-----PLOTTING----------------------------------
    fig = go.Figure()
    
    #Geometry
    clay_colour = stratum_geometry_rgb_df.loc[stratum_geometry_rgb_df["Name"]=="Clay", "hex_code"].iloc[0]
    sand_colour = stratum_geometry_rgb_df.loc[stratum_geometry_rgb_df["Name"]=="Sand", "hex_code"].iloc[0]
    #clay_colour = get_hex_colour("Clay")
    print(stratum_geometry_rgb_df.head())

    fig.add_trace(go.Scatter(x=clay_x, y=clay_y,
                    marker = dict(
                        color = clay_colour), #colorscale = clay_colour,
                    fill = "toself",
                    showlegend = False))
    fig.add_trace(go.Scatter(x=sand_x, y=sand_y,
                    marker = dict(
                    color = sand_colour),
                    fill = "toself",
                    showlegend = False))
    

    #Slip circle centres
    #fig = px.scatter(filtered_df, x="X", y="Y", color="Factor")
    fig.add_trace(go.Scatter(x=centre_points_x, y=centre_points_y, 
                       mode="markers", 
                       marker = dict(
                           colorscale = "Inferno",
                        color = filtered_df["Factor"],
                        showscale = True
                        ))) 
    
    #Slip circle arcs
    ### for each list_of_x in arc_x and each list_of_y in arc_y
    ##### plot a trace
    #fig.add_trace(go.Scatter(x=arc_x_list[1], y=arc_y_list[1]))
    for i in range(0,len(arc_df["arc_x"])):
        #fig = px.line(arc_df, x=["arc_x"][i], y=["arc_y"][i], color=)
        fig.add_trace(go.Scatter(x=arc_x_list[i], 
                        y=arc_y_list[i], 
                        mode ="lines",
                        showlegend = False,
                        line=dict(
                            color='firebrick',
                            width=1)))
    


    fig.update_yaxes(
    scaleanchor = "x",
    scaleratio = 1, 
    #fixedrange=True
    )    
    fig.update_layout(title_text = "Showing slip circles with a Factor between: \n" 
                        + str(input_lwr_value) + " and " 
                        + str(input_uppr_value))




#********************************************************
    
    #fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)