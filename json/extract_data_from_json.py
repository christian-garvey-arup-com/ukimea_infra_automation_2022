"""
SCRIPT TO EXTRACT DATA FROM A JSON FILE

AUTHOR: C GARVEY
DATE: 2021/12/10

"""
# Import the modules
import os
import json
import pandas as pd

#-----------------------------
# Get file path
cwd = os.getcwd()
dir = cwd
file_name = "Slope01_output.json" 
f = dir + "\\" + file_name
fo = open(f)

# Read data from file
data = json.loads(fo.read())
#print(json.dumps(data, indent=4))


#-----------------------------------------
#----------Extracting from JSON-----------
#-----------------------------------------

#-----------------------------------------
#### Strata data ####
#-----------------------------------------
# Read data from a json file
### Read strata point geometry -- Node > Point (all xyz data of drawn points - need to enumerate the Point dicts)
###                                  NB. Point indices start at 1!!!
### Write data to a dataframe [node_points_df]

#print(len(data["Node"]))
iter_nodes = len(data["Node"])

node_xyz = [
    data["Node"][i]["Point"] for i in range(iter_nodes)
    ]
#print(node_xyz)

#-----------------------------------------
# Read data from a json file
### Read strata topo geometry -- Member > Topo (startXY_node_point, endXY_node_point) --> Ignore dictionaries where "Name:" does not exist. Store as list of indices, indexed on "Name"
### Write data to a dataframe [member_topo_stratum_df]

#print(len(data["Member"]))
iter_member = len(data["Member"])

# Get series of nodes for each stratum - i.e. where "Name" exists in the dictionary 
stratum_nodes = [
    data["Member"][i]["Topo"] for i in range(iter_member) 
    if "Name" in data["Member"][i]
    ]
#print(stratum_nodes)

stratum_name = [
    data["Member"][i]["Name"] for i in range(iter_member) 
    if "Name" in data["Member"][i]
    ]
#print(stratum_name)

#***************************************
### Map stratum nodes to coordinates
# NB. Stratum_node = iter+1

stratum_nodes_int_list = []
stratum_xyz = []

# applies int() to the list of stratum_nodes elements
for index,value in enumerate(stratum_nodes):
    #print(index)        
    stratum_nodes_list = stratum_nodes[index].split()
    map_object = map(int, stratum_nodes_list)
    stratum_nodes_int = list(map_object)
    stratum_nodes_int_list.append(stratum_nodes_int)
#print(stratum_nodes_int_list)

# creates a list of coordinates for each stratum -- list of xyz dicts
for i in stratum_nodes_int_list:
    stratum_xyz_temp = []
    for j in i:
        #print (i)
        # NB. node_xyz index = stratum_node - 1
        node_dict = node_xyz[j-1]
        stratum_xyz_temp.append(node_dict)
    stratum_xyz.append(stratum_xyz_temp)
#print(stratum_xyz)


### Create a dataframe from Stratum name and XYZ nodes
# zip both lists together to create a df
stratum_geometry = list(zip(stratum_name, stratum_xyz))
#print(stratum_geometry)

## create DataFrame of stratum_name and stratum_xyz
stratum_geometry_df = pd.DataFrame(stratum_geometry, columns =["Name", "xyz"])
#print(stratum_geometry_df)





#-----------------------------------------
#### Material data ####
#-----------------------------------------
# Read data from a json file
### Read material data -- RunData > SlopeMaterials (extract all to df incl RGBStratum)
### Write data to a dataframe [materials_df]

#print(len(data["RunData"]["SlopeMaterials"]))
iter_materials = len(data["RunData"][0]["SlopeMaterials"])
#print(iter_materials)

material_data = [
    data["RunData"][0]["SlopeMaterials"][i] for i in range(iter_materials)
    ]
#print(material_data)
material_data_df = pd.DataFrame(material_data)



#-----------------------------------------
#### Slip surface data ####
#-----------------------------------------
# Read data from a json file
### Read slip surfaces data -- RunData > Slope results > 
# [ignore dictionaries where 'Radius' = 0], extract SlipWeight, Factor, Disturbing, Restoring, Points[centre, top, bottom] as columns.
### Write data to a dataframe

#print(len(data["RunData"]["Slope results"]))
iter_results = len(data["RunData"][0]["Slope results"])
#print(iter_results)

results_data = []
result_keys = ["SlipWeight", "Factor", "Disturbing", "Restoring", "Points"]
for i in range(iter_results):
    if data["RunData"][0]["Slope results"][i]["Radius"] > 0:
        results_dict = data["RunData"][0]["Slope results"][i]
        results_dict_reduced = dict((key, results_dict[key]) for key in result_keys if key in results_dict)
        results_data.append(results_dict_reduced)
#print(results_data)
results_data_df = pd.DataFrame(results_data)


from functions import slope_results_df
print(slope_results_df(data, iter_results, result_keys))


#-----------------------------------------
#----------Manipulation-------------------
#-----------------------------------------

# Data has now been split into dataframes and is ready to be brought into the dashboard.




