### Read strata topo geometry 
### Map stratum nodes to coordinates

# NB. Stratum_node = iter+1

stratum_nodes= ['8 7 6 5 4 3 2', '2 9 10 11 12 13']
node_xyz = [{'X': -25, 'Y': 60, 'Z': 0}, 
            {'X': 0, 'Y': 20, 'Z': 0}, 
            {'X': 0, 'Y': 0, 'Z': 0}, 
            {'X': 50, 'Y': 0, 'Z': 0}, 
            {'X': 50, 'Y': 5, 'Z': 0}, 
            {'X': 50, 'Y': 10, 'Z': 0}, 
            {'X': 35, 'Y': 10, 'Z': 0}, 
            {'X': 30, 'Y': 15, 'Z': 0}, 
            {'X': 0, 'Y': 35, 'Z': 0}, 
            {'X': 10, 'Y': 35, 'Z': 0}, 
            {'X': 15, 'Y': 25, 'Z': 0}, 
            {'X': 20, 'Y': 20, 'Z': 0}, 
            {'X': 30, 'Y': 15, 'Z': 0}
            ]

stratum_nodes_int_list = []
stratum_xyz = []

# applies int() to a list of elements
for index,value in enumerate(stratum_nodes):
    #print(index)        
    stratum_nodes_list = stratum_nodes[index].split()
    map_object = map(int, stratum_nodes_list)
    stratum_nodes_int = list(map_object)
    # add the start node to the end of the list -- close the stratum polygon
    stratum_nodes_int.append(stratum_nodes_int[0])
    stratum_nodes_int_list.append(stratum_nodes_int)
print(stratum_nodes_int_list)

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




#------------------------------
### JSON NORMALISER
#------------------------------
#print(pd.json_normalize(data, record_path="RunData", meta="SlopeMaterials", errors="ignore"))