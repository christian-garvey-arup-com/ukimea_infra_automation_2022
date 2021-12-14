import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc, html
from dash.dependencies import Input, Output
import dash
import sys
from plotly.tools import mpl_to_plotly
#import matplotlib.collections as coll

#------------------------------------
### CREATING SLOPE PLOT -- app.py ###
#------------------------------------

sys.path.append('C:/Users/christian.garvey/OneDrive - Arup/01 Documents/01-07 Digital/Python/ukimea-automation-training-2022/Individual_project/individual_project_cgarvey/json/')
import extract_data_from_json 
#print(extract_data_from_json.stratum_geometry_df)

df = extract_data_from_json.results_data_df
"""
filtered_df = df[df["Factor"] <= 1]
#print(filtered_df)
# For each row
### For first dict
##### Read 'X' 

#centre points are at Slope Results['X'] and ['Y'] 
centre_points_x = filtered_df["X"]
centre_points_y = filtered_df["Y"]


#centre_x = [i for i in filtered_df["Points"][0]['X']] 

#fig = px.scatter(filtered_df, x=centre_points_x, y=centre_points_y) 
#fig = plt.scatter(x=centre_points_x, y=centre_points_y) 
plt.show()

# fig = plt.patches.Arc() 
#     data=[go.matplotlib [0,1,2,3,4])



"""


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


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='plot_title', value='Type title...', type="text"),
    dcc.Slider(
        id='box_size',
        min=1,
        max=10,
        value=4,
        step=1
        #marks=list(range(0, 10))
    ),
    html.Div([html.Img(id = 'cur_plot', src = '')])
             #id='plot_div')
])

@app.callback(
    Output(component_id='cur_plot', component_property='src'),
    [Input(component_id='plot_title', component_property='value'), Input(component_id = 'box_size', component_property='value')]
)
def update_graph(input_value, n_val):
    fig, ax1 = plt.subplots(1,1)
    np.random.seed(len(input_value))
    ax1.matshow(np.random.uniform(-1,1, size = (n_val,n_val)))
    ax1.set_title(input_value)
    out_url = fig_to_uri(fig)
    #fig.update_layout(transition_duration=500)
    return out_url

app.run_server(debug=True)






#**********************************************
#***EXTRACT SLIP CIRCLE POINTS***
#**********************************************

#Slip circle left_points are at Points row[1], right_points are at Points row[2]
# centre_points_x = []
# for row in filtered_df["Points"]:
#     for row[0] in row:
#         #print (row[0])
#         for k,v in row[0].items():
#             if k=='X':
#                 centre_points_x.append(v)
#                 #print(k,v)