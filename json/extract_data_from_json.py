"""
SCRIPT TO EXTRACT DATA FROM A JSON FILE

AUTHOR: C GARVEY
DATE: 2021/12/10

"""
# Import the modules
import os
import json
from sys import path
import pandas as pd
from pathlib import Path
#-----------------------------------------
#---------- Get data----------------------
#-----------------------------------------
file_name = "Slope01_output.json" 
dir = r"C:\Users\christian.garvey\OneDrive - Arup\01 Documents\01-07 Digital\Python\ukimea-automation-training-2022\Individual_project\individual_project_cgarvey"
from functions_json import get_json_data, rgbint_to_hex
data = (get_json_data(file_name, dir))



#-----------------------------------------
#----------Extracting from JSON-----------
#-----------------------------------------
from functions_json import extract_json_data
#Dive into function to change variables.

stratum_geometry_df = extract_json_data(data)[0]
material_data_df = extract_json_data(data)[1]
slope_output_df = extract_json_data(data)[2]
   


#-----------------------------------------
#----------Manipulation-------------------
#-----------------------------------------
# Merge RGBInt colours from materials to stratum geometry df
stratum_geometry_rgb_df = pd.merge(stratum_geometry_df, material_data_df[["Name", "RGBStratum"]], on="Name", how="left")
stratum_geometry_rgb_df["hex_code"] = [rgbint_to_hex(i) for i in stratum_geometry_rgb_df["RGBStratum"]]

# Data has now been split into dataframes and is ready to be brought into the dashboard.




