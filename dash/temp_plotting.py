# #--------------------------------------------
# # To create points along an arc
# #--------------------------------------------

# #https://stackoverflow.com/questions/48603681/plot-arc-path-between-two-points

# from math import pi, hypot, sin, cos, atan2, degrees
# import matplotlib.pyplot as plt
# import plotly.express as px

# def norm_angle(a):
#     # Normalize the angle to be between -pi and pi
#     return (a+pi)%(2*pi) - pi

# # Given values
# # named just like in http://rossum.sourceforge.net/papers/CalculationsForRobotics/CirclePath.htm
# x_0, y_0 = [0,0] # initial position of robot
# theta_0 = -pi/2      # initial orientation of robot
# s = 0.5               # speed of robot
# x_1, y_1 = [10,30] # goal position of robot
# t_0 = 0              # starting time

# # To be computed:
# r_G = hypot(x_1 - x_0, y_1 - y_0)        # relative polar coordinates of the goal
# phi_G = atan2(y_1 - y_0, x_1 - x_0)
# phi = 2*norm_angle(phi_G - theta_0)      # angle and 
# r_C = r_G/(2*sin(phi_G - theta_0))       # radius (sometimes negative) of the arc
# L = r_C*phi                              # length of the arc
# if phi > pi:
#     phi -= 2*pi
#     L = -r_C*phi
# elif phi < -pi:
#     phi += 2*pi
#     L = -r_C*phi
# t_1 = L/s + t_0                        # time at which the robot finishes the arc
# omega = phi/(t_1 - t_0)                # angular velocity           
# x_C = x_0 - r_C*sin(theta_0)           # center of rotation
# y_C = y_0 + r_C*cos(theta_0)

# # list_x = []
# # def position(t):
# #     x = x_C + r_C*sin(omega*(t - t_0) + theta_0)
# #     y = y_C - r_C*cos(omega*(t - t_0) + theta_0)
# #     return x, y
# # def orientation(t):
# #     return omega*(t - t_0) + theta_0




# list_x = []
# list_y = []
# for t in range(t_0, int(t_1)+1):
#     x = x_C + r_C*sin(omega*(t - t_0) + theta_0)
#     list_x.append(x)
#     y = y_C - r_C*cos(omega*(t - t_0) + theta_0)
#     list_y.append(y)

# print(list_x, list_y)

# #fig, ax = plt.subplots()
# #ax.scatter(x=list_x, y=list_y)
# fig = px.line(x=list_x,y=list_y)
# fig.update_yaxes(
#     scaleanchor = "x",
#     scaleratio = 1,
#   )
# fig.show()



#**********************************************
#***EXTRACT SLIP CIRCLE POINTS***
#**********************************************

# import sys
# sys.path.append('C:/Users/christian.garvey/OneDrive - Arup/01 Documents/01-07 Digital/Python/ukimea-automation-training-2022/Individual_project/individual_project_cgarvey/json/')
# import extract_data_from_json
# df = extract_data_from_json.slope_output_df

# filtered_df = df[(df["Factor"] >= 1) & (df["Factor"] <= 10)]


# #centre points are at Slope Results['X'] and ['Y'] 
# centre_points_x = filtered_df["X"]
# centre_points_y = filtered_df["Y"]

# #Slip circle left_points are at Points row[1], right_points are at Points row[2]
# def get_arc_intersection_points(dataframe_col:list, item_index, coordinate:str):
#     """
#     """
#     points_list = []
#     for row in dataframe_col:
#         for row[item_index] in row:
#             for k,v in row[item_index].items():
#                 if k==coordinate:
#                     points_list.append(v)
#     return points_list

# start_x = get_arc_intersection_points(filtered_df["Points"], 1, "X")
# start_y = get_arc_intersection_points(filtered_df["Points"], 1, "Y")
# end_x = get_arc_intersection_points(filtered_df["Points"], 2, "X")
# end_y = get_arc_intersection_points(filtered_df["Points"], 2, "Y")

# #print(len(end_y))

# # for i in start_x:
# #     print (i)#,j,k,l)
# # for i in start_x,start_y,end_x,end_y:
# #     print (start_x[100])

# import time
# t0 = time.perf_counter()
# counter = 0
# for i in range(0,len(start_x)):
#     #print("here")
#     arc_points(start_x[i],start_y[i],end_x[i],end_y[i],0.1)
#     counter += 1
# print(counter)
# t1 = time.perf_counter()
# print(f"Downloaded the tutorial in {t1 - t0:0.4f} seconds")
