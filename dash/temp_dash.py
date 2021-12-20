import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame
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

# sys.path.append('C:/Users/christian.garvey/OneDrive - Arup/01 Documents/01-07 Digital/Python/ukimea-automation-training-2022/Individual_project/individual_project_cgarvey/json/')
# import extract_data_from_json 
# #print(extract_data_from_json.stratum_geometry_df)

# df = extract_data_from_json.results_data_df
# """
# filtered_df = df[df["Factor"] <= 1]
# #print(filtered_df)
# # For each row
# ### For first dict
# ##### Read 'X' 

# #centre points are at Slope Results['X'] and ['Y'] 
# centre_points_x = filtered_df["X"]
# centre_points_y = filtered_df["Y"]


# #centre_x = [i for i in filtered_df["Points"][0]['X']] 

# #fig = px.scatter(filtered_df, x=centre_points_x, y=centre_points_y) 
# #fig = plt.scatter(x=centre_points_x, y=centre_points_y) 
# plt.show()

# # fig = plt.patches.Arc() 
# #     data=[go.matplotlib [0,1,2,3,4])



# """


# import matplotlib.pyplot as plt
# import numpy as np
# from io import BytesIO
# import base64
# def fig_to_uri(in_fig, close_all=True, **save_args):
#     # type: (plt.Figure) -> str
#     """
#     Save a figure as a URI
#     :param in_fig:
#     :return:
#     """
#     out_img = BytesIO()
#     in_fig.savefig(out_img, format='png', **save_args)
#     if close_all:
#         in_fig.clf()
#         plt.close('all')
#     out_img.seek(0)  # rewind file
#     encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
#     return "data:image/png;base64,{}".format(encoded)


# app = dash.Dash(__name__)

# app.layout = html.Div([
#     dcc.Input(id='plot_title', value='Type title...', type="text"),
#     dcc.Slider(
#         id='box_size',
#         min=1,
#         max=10,
#         value=4,
#         step=1
#         #marks=list(range(0, 10))
#     ),
#     html.Div([html.Img(id = 'cur_plot', src = '')])
#              #id='plot_div')
# ])

# @app.callback(
#     Output(component_id='cur_plot', component_property='src'),
#     [Input(component_id='plot_title', component_property='value'), Input(component_id = 'box_size', component_property='value')]
# )
# def update_graph(input_value, n_val):
#     fig, ax1 = plt.subplots(1,1)
#     np.random.seed(len(input_value))
#     ax1.matshow(np.random.uniform(-1,1, size = (n_val,n_val)))
#     ax1.set_title(input_value)
#     out_url = fig_to_uri(fig)
#     #fig.update_layout(transition_duration=500)
#     return out_url

# app.run_server(debug=True)






# #**********************************************
# #***EXTRACT SLIP CIRCLE POINTS***
# #**********************************************

# #Slip circle left_points are at Points row[1], right_points are at Points row[2]
# def get_arc_intersection_points(dataframe_col:list, item_index, coordinate:str):
#     """
#     Slip circle left_points are at Points row[1], right_points are at Points row[2]
#     """
#     points_list = []
#     for row in dataframe_col:
#         for row[item_index] in row:
#             for k,v in row[item_index].items():
#                 if k==coordinate:
#                     points_list.append(v)
#     return points_list


#***********************************************
# import sys
# sys.path.append('C:/Users/christian.garvey/OneDrive - Arup/01 Documents/01-07 Digital/Python/ukimea-automation-training-2022/Individual_project/individual_project_cgarvey/json/')
# import extract_data_from_json
# df = extract_data_from_json.slope_output_df

# arc_x_list = []
# arc_y_list = []


# def print_arc_lists():    

#     start_x = df["arc_start_x"]
#     start_y = df["arc_start_y"]
#     end_x = df["arc_end_x"]
#     end_y = df["arc_end_y"]

#     # arc_x_list = []
#     # arc_y_list = []

#     ### Calculate points along an arc for each start xy and end xy.
#     from functions_dash import arc_points
#     ### Pass 4 coordinates to arc_points per iteration
#     for i in range(0, 2): #len(start_x)):     # len start_x is arbitrary
#         print(start_x[i])
#         #global arc_x_list
#         # x_pts = arc_points(start_x[i],start_y[i],end_x[i],end_y[i],0.5)[0]
#         # print(x_pts)
#         # arc_x_list.append(x_pts)
    
#         # y_pts = arc_points(start_x[i],start_y[i],end_x[i],end_y[i],0.5)[1]
#         # print(y_pts)
#         # arc_y_list.append(y_pts)
#     # print(arc_x_list)
#     # print(arc_y_list)
#         #print(arc_x_list_1)
#         #arc_x_list_1 = arc_x_list.append(arc_points(start_x[i],start_y[i],end_x[i],end_y[i],0.5)[0])
#         #global arc_y_list 
#         #arc_y_list_1 = arc_y_list.append(arc_points(start_x[i],start_y[i],end_x[i],end_y[i],0.5)[1])

#         # print(arc_points(start_x[i],start_y[i],end_x[i],end_y[i],0.5)[1])
#         # print(arc_x_list_1)
#         # print(arc_y_list_1)
#     # print(len(start_x))
#     # print(len(start_y))
#     # print(df.head())
#     # print(start_x)
#     # print(start_y)
# print_arc_lists()

from functions_dash import arc_points
print(arc_points(0.02502, 35, 26.096,16.952, 0.5))
