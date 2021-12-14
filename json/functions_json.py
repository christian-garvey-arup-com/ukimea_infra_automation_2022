#-----------------------------------------
#----------LIBRARIES FOR FUNCTIONS--------
#-----------------------------------------
import json
import pandas as pd
import math

#-----------------------------------------
#----------Extracting from JSON-----------
#-----------------------------------------
def extract_json_data(data:json):
    """Generates dataframes for: 
    strata geometry (e.g. xyz coordinates of nodes), 
    materials data (e.g. c', phi'), 
    slope results (e.g. slip circles, factor of safety)
    Returns a pandas dataframe for each of the above.
    NB. Contains functions.
    """
    #Strata data
    from functions_json import get_nested_data
    ##Iterate through "Nodes"
    iter_nodes = len(data["Node"])
    node_xyz = get_nested_data(data, "Node", "Point", iter_nodes)
    ##Iterate through "Members"
    iter_member = len(data["Member"])
    stratum_nodes = get_nested_data(data,"Member", "Topo", iter_member, "Name", "Member")
    stratum_name = get_nested_data(data,"Member", "Name", iter_member, "Name", "Member")

    from functions_json import get_stratum_nodes_int
    stratum_nodes_int_list = get_stratum_nodes_int(stratum_nodes)
    
    from functions_json import get_stratum_nodes_xyz
    stratum_xyz = get_stratum_nodes_xyz(stratum_nodes_int_list, node_xyz)
    stratum_geometry = list(zip(stratum_name, stratum_xyz))
    stratum_geometry_df = pd.DataFrame(stratum_geometry, columns =["Name", "xyz"])

    #Material data
    ##Iterate through "SlopeMaterials"
    iter_materials = len(data["RunData"][0]["SlopeMaterials"])
    material_data = [
        data["RunData"][0]["SlopeMaterials"][i] for i in range(iter_materials)
        ]   
    material_data_df = pd.DataFrame(material_data)

    #Slope results data
    ##Iterate through "Slope results"
    from functions_json import slope_results_df
    iter_results = len(data["RunData"][0]["Slope results"])
    result_keys = ["SlipWeight", "X", "Y", "Factor", "Disturbing", "Restoring", "Points"]
    slope_output_df = slope_results_df(data, iter_results, result_keys)


    return stratum_geometry_df, material_data_df, slope_output_df


#-----------------------------------------

## FUNCTION TO IMPORT THE JSON FILE
def get_json_data(file_name:str, dir:str):
    """Returns JSON data from the file in a format which is ready to ingest in python. 
    Uses 'json.loads()'. 
    Requires the following library:
            json
    Inputs:
    file_name (str): file name of the json file (no backslash at beginning)
    dir (str):     
    """
    f = dir + "\\" + file_name
    fo = open(f)
    # Read data from file
    data = json.loads(fo.read())

    return data



## FUNCTION TO EXTRACT DATA FROM A NESTED DICTIONARY
def get_nested_data(data:json, level1_name:str, level2_name:str, iter_range:int, child=None, parent=None):
    """Extracts a list of nested data, two levels deep
    data: a unloaded json file (e.g. data = json.loads(fo.read()))
    Returns a list.
    child: optional -- allows filtering of data
    parent: optional -- allows filtering of data
    E.g. stratum_nodes = [
    data["Member"][i]["Topo"] for i in range(iter_member) 
    if "Name" in data["Member"][i]
    ]
    """
    if child != None and parent != None:
            data_list = [data[level1_name][i][level2_name] for i in range(iter_range)
    if child in data[parent][i] 
    ]        
    elif (child != None and parent == None) or (child == None and parent != None):
        KeyError("Expected 2 arguments (for 'child' and 'parent'). Got only 1.") 
    else:    
        data_list = [data[level1_name][i][level2_name] for i in range(iter_range)] 
    
    return data_list


## FUNCTION TO CONVERT STRATUM NODES TO LIST OF INTEGERS
def get_stratum_nodes_int(stratum_nodes):
    """Returns a list of nodes as integers for each stratum (i.e. parses each string of node indices from 'stratum_nodes')
    -- Returns a list.
    stratum_nodes: a string of node indices (e.g. ['8 7 6 5 4 3 2', '2 9 10 11 12 13'])
    """
    # applies int() to the list of stratum_nodes elements
    stratum_nodes_int_list = []
    for index,value in enumerate(stratum_nodes):      
        stratum_nodes_list = stratum_nodes[index].split()
        map_object = map(int, stratum_nodes_list)
        stratum_nodes_int = list(map_object)
        # add the start node to the end of the list -- close the stratum polygon
        stratum_nodes_int.append(stratum_nodes_int[0])
        stratum_nodes_int_list.append(stratum_nodes_int)
    # return a list of nodes as integers for each stratum (i.e. each string of node indices from stratum_nodes)
    return stratum_nodes_int_list



## FUNCTION TO CREATE A LIST OF COORDINATES FOR EACH STRATUM
def get_stratum_nodes_xyz(stratum_nodes_int_list, node_xyz):    
    """Returns a list of xyz coordinates of each node for each stratum. 
    To be called in conjunction with 'get_stratum_node_int' fn. 
    -- Returns a list of xyz coordinates as dicts
    stratum_node_int_list: returned object from 'get_stratum_node_int'
    node_xyz: xyz coordinates of each node, stored as a list of dictionaries (e.g. node_xyz = [{'X': -25, 'Y': 60, 'Z': 0}, {'X': 0, 'Y': 20, 'Z': 0}])
    """
    stratum_xyz = []
    for i in stratum_nodes_int_list:
        stratum_xyz_temp = []
        for j in i:
            # NB. The node indices as reported in Slope json file have a base of 1.
            # ...So, node_xyz index = stratum_node - 1
            node_dict = node_xyz[j-1]
            stratum_xyz_temp.append(node_dict)
        stratum_xyz.append(stratum_xyz_temp)
    # return a list of xyz coordinates for each node for each stratum
    return stratum_xyz


## FUNCTION TO CREATE A DATAFRAME FROM SLOPE RESULTS DATA
def slope_results_df(data, iter_results, result_keys):
    """Returns a dataframe of the selected data from the Slope Results json data. 
    -- Requires pandas to be imported as 'pd'.
    data: a unloaded json file (e.g. data = json.loads(fo.read()))
    iter_results: number of slope results to iterate through
    result_keys: list of strings of dictionary keys to extract data from (e.g. ["SlipWeight", "Factor", "Disturbing", "Restoring", "Points"])
    """
    results_data = []
    for i in range(iter_results):
        if data["RunData"][0]["Slope results"][i]["Radius"] > 0:
            results_dict = data["RunData"][0]["Slope results"][i]
            results_dict_reduced = dict((key, results_dict[key]) for key in result_keys if key in results_dict)
            results_data.append(results_dict_reduced)
    results_data_df = pd.DataFrame(results_data)
    return results_data_df



## FUNCTION TO TRANSFORM OASYS COLOUR CODE TO HTML
def to_hex_code(oasys_colour_code):
    """Returns the hexadecmial colour code from the Oasys Slope colour code (represented as an RGB-int code).
    Converts RGB-int to hexadecimal.
    oasys_colour_code: RGB-int code e.g. SlopeMaterials > "RGBStratum": 14745599
    """
    hex_string = (hex(oasys_colour_code))
    # remove "0x" from start of hex_string, and add a "#" 
    hex_string = "#" + hex_string[2:]
    return hex_string


## FUNCTIONS TO TRANSFORM OASYS COLOUR CODE TO HEX (FOR HTML)
def rgbint_to_rgb(oasys_colour_code):
    """Returns the RGB colour code from the Oasys Slope colour code (RGB-int)
    Converts RGB-int to RGB.
    Requires the following libraries:
        import math
    oasys_colour_code: RGB-int code e.g. SlopeMaterials > "RGBStratum": 14745599
    """
    b = math.floor((oasys_colour_code/65536))
    g = math.floor((oasys_colour_code%65536)/256)
    r = (oasys_colour_code%65536)-(g*256)
    return r,g,b
#print(rgbint_to_rgb(14745599))

def rgb_to_hex(rgb):
    """Returns the hexadecimal representation of the RGB(r,g,b) colour code
    rgb: tuple of RGB values e.g. (255,255,224)
    """
    hex_string = '#%02x%02x%02x' % rgb
    return hex_string

def rgbint_to_hex(oasys_colour_code):
    """Returns the hexideciamal representation of the Oasys Slope colour code (RGB-int)
    Converts RGB-int to hex.
    Requires the following libraries:
        import math
    oasys_colour_code: RGB-int code e.g. SlopeMaterials > "RGBStratum": 14745599
    output: hex e.g. #ffffe0
    """
    b = math.floor((oasys_colour_code/65536))
    g = math.floor((oasys_colour_code%65536)/256)
    r = (oasys_colour_code%65536)-(g*256)
    rgb = (r,g,b)
    hex_string = '#%02x%02x%02x' % rgb
    return hex_string

# oasys_colour_code = 14745599 # should be: #ffffe0
# print(rgbint_to_hex(oasys_colour_code))
