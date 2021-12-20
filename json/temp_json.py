### Read strata topo geometry 
### Map stratum nodes to coordinates

# NB. Stratum_node = iter+1

# stratum_nodes= ['8 7 6 5 4 3 2', '2 9 10 11 12 13']
# node_xyz = [{'X': -25, 'Y': 60, 'Z': 0}, 
#             {'X': 0, 'Y': 20, 'Z': 0}, 
#             {'X': 0, 'Y': 0, 'Z': 0}, 
#             {'X': 50, 'Y': 0, 'Z': 0}, 
#             {'X': 50, 'Y': 5, 'Z': 0}, 
#             {'X': 50, 'Y': 10, 'Z': 0}, 
#             {'X': 35, 'Y': 10, 'Z': 0}, 
#             {'X': 30, 'Y': 15, 'Z': 0}, 
#             {'X': 0, 'Y': 35, 'Z': 0}, 
#             {'X': 10, 'Y': 35, 'Z': 0}, 
#             {'X': 15, 'Y': 25, 'Z': 0}, 
#             {'X': 20, 'Y': 20, 'Z': 0}, 
#             {'X': 30, 'Y': 15, 'Z': 0}
#             ]

# stratum_nodes_int_list = []
# stratum_xyz = []

# # applies int() to a list of elements
# for index,value in enumerate(stratum_nodes):
#     #print(index)        
#     stratum_nodes_list = stratum_nodes[index].split()
#     map_object = map(int, stratum_nodes_list)
#     stratum_nodes_int = list(map_object)
#     # add the start node to the end of the list -- close the stratum polygon
#     stratum_nodes_int.append(stratum_nodes_int[0])
#     stratum_nodes_int_list.append(stratum_nodes_int)
# print(stratum_nodes_int_list)

# # creates a list of coordinates for each stratum -- list of xyz dicts
# for i in stratum_nodes_int_list:
#     stratum_xyz_temp = []
#     for j in i:
#         #print (i)
#         # NB. node_xyz index = stratum_node - 1
#         node_dict = node_xyz[j-1]
#         stratum_xyz_temp.append(node_dict)
#     stratum_xyz.append(stratum_xyz_temp)
# #print(stratum_xyz)
# #print(stratum_xyz[0][0]["X"])



# # Demonstration to extract all x-coordinates for a stratum from the df
# clay = stratum_geometry_df[stratum_geometry_df['Name'] == "Clay"]
# #print(clay['xyz'][0][0]['X'])

# iter_x = len(clay['xyz'][0])
# print(iter_x)
# clay_x = [
#     clay['xyz'][0][i]['X'] for i in range(iter_x)
#     ]
# print(clay_x)



# creates a list of coordinates for each stratum -- list of xyz lists.
# for i in stratum_nodes_int_list:
#     stratum_xyz_temp = []
#     for j in i:
#         #print (i)
#         # NB. node_xyz index = stratum_node - 1
#         node_dict = node_xyz[j-1]
#         node_values = list(node_dict.values())
#         stratum_xyz_temp.append(node_values)
#     stratum_xyz.append(stratum_xyz_temp)
# print(stratum_xyz)



#------------------------------
# RESULTS

# iter_results = len(data["RunData"][0]["Slope results"])
# #print(iter_results)

# results_data = [
#     data["RunData"][0]["Slope results"][i]["SlipWeight"] for i in range(iter_results)
#     if data["RunData"][0]["Slope results"][i]["Radius"] > 0 
#     ]
# #print(results_data)
# results_data_df = pd.DataFrame(results_data)

# #res = dict((k, test_dict[k]) for k in ['nikhil', 'akshat'] if k in test_dict)



# coffees_sold = ["Espresso", "Espresso", "Latte", "Cappuccino", "Mocha", "Espresso", "Latte"]

# def count_coffees(coffees, to_find=None):
#     if to_find == None:
#         print(coffees)
#     else: 
#         number_sold = coffees.count(to_find)
#         print("{} {} coffees were sold.".format(number_sold, to_find))
#     return
# print(count_coffees(coffees_sold))



# file_name = "Slope01_output.json" 
# dir = r"C:\Users\christian.garvey\OneDrive - Arup\01 Documents\01-07 Digital\Python\ukimea-automation-training-2022\Individual_project\individual_project_cgarvey"
# from functions_json import get_json_data
# data = (get_json_data(file_name, dir))

# import json
# def get_nested_data(data:json, level1_name:str, level2_name:str, iter_range:int, child=None, parent=None):
#     """Extracts a list of nested data, two levels deep
#     data: a unloaded json file (e.g. data = json.loads(fo.read()))
#     Returns a list.
#     child: optional -- allows filtering of data
#     parent: optional -- allows filtering of data
#     E.g. stratum_nodes = [
#     data["Member"][i]["Topo"] for i in range(iter_member) 
#     if "Name" in data["Member"][i]
#     ]
#     """
#     if child != None and parent != None:
#             data_list = [data[level1_name][i][level2_name] for i in range(iter_range)
#     if child in data[parent][i] 
#     ]        
#     elif (child != None and parent == None) or (child == None and parent != None):
#         KeyError("Expected 2 arguments (for 'child' and 'parent'). Got only 1.") 
#     else:    
#         data_list = [data[level1_name][i][level2_name] for i in range(iter_range)] 
    
#     return data_list


# iter_member = len(data["Member"])
# # Get series of nodes for each stratum - i.e. where "Name" exists in the dictionary 
# stratum_nodes = get_nested_data(data,"Member", "Topo", iter_member, "Name", "Member")
# iter_nodes = len(data["Node"])
# node_xyz = get_nested_data(data, "Node", "Point", iter_nodes)
# #print(node_xyz)

# from functions_json import get_stratum_nodes_int
# stratum_nodes_int_list = get_stratum_nodes_int(stratum_nodes)
# print(stratum_nodes_int_list)


# from functions_json import get_stratum_nodes_xyz
# print(get_stratum_nodes_xyz(stratum_nodes_int_list, node_xyz))

# iter_results = len(data["RunData"][0]["Slope results"])
# result_keys = ["SlipWeight", "X", "Y", "Factor", "Disturbing", "Restoring", "Points"]

# from functions_json import slope_results_df
# print(slope_results_df(data, iter_results, result_keys))

#------------------------------
### JSON NORMALISER
#------------------------------
#print(pd.json_normalize(data, record_path="RunData", meta="SlopeMaterials", errors="ignore"))

#------------------------------
### EXPAND LIST OF DICTS FROM DF
#------------------------------
import pandas as pd
from pandas.core.frame import DataFrame
file_name = "Slope01_output.json" 
dir = r"C:\Users\christian.garvey\OneDrive - Arup\01 Documents\01-07 Digital\Python\ukimea-automation-training-2022\Individual_project\individual_project_cgarvey"
from functions_json import get_json_data
data = (get_json_data(file_name, dir))

# from functions_json import slope_results_df
# iter_results = len(data["RunData"][0]["Slope results"])
# result_keys = ["SlipWeight", "X", "Y", "Factor", "Disturbing", "Restoring", "Points"]
# slope_output_df = slope_results_df(data, iter_results, result_keys)

# from functions_json import get_arc_intersection_points
# start_X = get_arc_intersection_points(slope_output_df["Points"], 1, "X") #==> slope_output_df["Point_start_x"]

# slope_output_df["arc_start_x"] = get_arc_intersection_points(slope_output_df["Points"], 1, "X")
# slope_output_df["arc_start_x"] = get_arc_intersection_points(slope_output_df["Points"], 1, "X")

# print(slope_output_df.head())


from functions_json import extract_json_data
stratum_geometry_df = extract_json_data(data)[0]
material_data_df = extract_json_data(data)[1]
print(stratum_geometry_df.head())
print(material_data_df.head())

from functions_json import rgbint_to_hex

# points_list = []
# coordinate = "X"
# for i in stratum_geometry_df['xyz'][0]:
#     for k,v in i.items():
#         if k==coordinate:
#             points_list.append(v)
# print(points_list)
# stratum_name = stratum_geometry_df['Name'][0]

# stratum_data = {: points_list}



# # # Demonstration to extract all x-coordinates for a stratum from the df

# def get_strata_list(df:DataFrame, strata_name:str, coordinate:str):
#     subset_df = df[df['Name'] == strata_name]
#     iter = len(subset_df['xyz'][0])
#     strata_list = [
#         subset_df['xyz'][0][i][coordinate] for i in range(iter)
#         ]
#     return strata_list

# subset_df = stratum_geometry_df[stratum_geometry_df['Name'] == "Sand"]
# print(subset_df)
# iter_cell = subset_df.loc[subset_df['Name'] == 'Sand', 'xyz'].iloc[0]
# iter = len(iter_cell)
# print(iter)
# strata_list = [
#     iter_cell[i]["X"] for i in range(iter)
#     ]
# print(strata_list)

from functions_json import get_strata_list
# clay_x = get_strata_list(stratum_geometry_df, "Clay","X")
# clay_y = get_strata_list(stratum_geometry_df, "Clay","Y")
# sand_x = get_strata_list(stratum_geometry_df, "Sand","X")
# sand_y = get_strata_list(stratum_geometry_df, "Sand","Y")
# print(clay_y)

stratum_geometry_rgb_df = pd.merge(stratum_geometry_df, material_data_df[["Name", "RGBStratum"]], on="Name", how="left")
print(stratum_geometry_rgb_df)


stratum_geometry_rgb_df["hex_code"] = [rgbint_to_hex(i) for i in stratum_geometry_rgb_df["RGBStratum"]]
print(stratum_geometry_rgb_df)
print(stratum_geometry_rgb_df.loc[stratum_geometry_rgb_df["Name"]=="Clay", "hex_code"].iloc[0])