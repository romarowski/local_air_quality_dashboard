import pandas as pd
import os 
import numpy as np
import pdb

data = pd.read_csv('data/environment_input_data/1h.csv')
data8 = pd.read_csv('data/environment_input_data/8h.csv')
data24 = pd.read_csv('data/environment_input_data/24h.csv')
limits = pd.read_csv('data/environment_input_data/limits.csv')
runway_loc = pd.read_csv('data/environment_input_data/location_runway.csv')
pollutant_name = []
#pdb.set_trace()
pollutants = data.columns

#pollutants = [' USAQI', 'CO₂ (ppm)', 'CO (mg/m³)',
#       'NO₂ (µg/m³ )', 'O₃ (µg/m³ )', 'H₂S (µg/m³ )', 'NO (µg/m³ )',
#       'SO₂ (µg/m³)', 'R. Humidity (%)', 'Leq (dB)', 'Light (Lux)',
#       'Lmax (dB)', 'Lmin (dB)', 'Temperature (°C)', 
#       'PM₂.₅ (µg/m³ )', 'PM₁₀ (µg/m³)', 'UV ( Index)',
#       'PM₁ (µg/m³ )', 'Wind Speed (km/h)']
       

pollutants = ['AQI', 'Temperature (°C)', 'R. Humidity (%)',  
        'CO (mg/m³)','NO₂ (µg/m³ )','O₃ (µg/m³ )','SO₂ (µg/m³)',
        'PM₂.₅ (µg/m³ )','PM₁₀ (µg/m³)',#'PM₁ (µg/m³ )', 
        'CO₂ (ppm)',
        'H₂S (µg/m³ )', 'NO (µg/m³ )','Leq (dB)', 'Lmin (dB)', 'Lmax (dB)']

for pollutant in pollutants:
    pollutant_name.append(pollutant.split(' (', 1)[0])

pollutant_name[0] = 'AQI'

#------------------SCRIPT FOR DATA WRANGLING ONLY RUN ONCE---------------###


#input_data_df_list = []
#
#directory = r'data/24h'
#input_files = os.listdir(directory)
#sep = ' 24 Hours Avg.csv' #Set separation for file_names
#
#for file_name in input_files:
#    station_name = file_name.split(sep, 1)[0]
#    file_dir = directory + '/' + file_name
#    df = pd.read_csv(file_dir)
#    df = df.assign(Station = station_name)
#    input_data_df_list.append(df)
#
## Creates a huge df with all data
#data = pd.concat(input_data_df_list).fillna(0)
## Adds the month column
#data["Month"] = pd.DatetimeIndex(data["To Date"]).month_name()
#data["Month Index"] = pd.DatetimeIndex(data["To Date"]).month
#data["Day"] = pd.DatetimeIndex(data["To Date"]).day_name()
#data["Day Index"] = pd.DatetimeIndex(data["To Date"]).dayofweek
#data["Hour"] = pd.DatetimeIndex(data["To Date"]).hour
#data["Date"] = pd.DatetimeIndex(data["To Date"]).date
#
## Data wrangling for windrose
#data['Wind Speed (m/s)'] = pd.to_numeric(data['Wind Speed (m/s)'], errors='coerce')
#data['Wind Direction (degree)'] = pd.to_numeric(data['Wind Direction (degree)'], errors='coerce')
#data['Wind Speed (km/h)'] = data['Wind Speed (m/s)']*3.6
##data['Wind Speed (km/h)'] = data[data['Wind Speed (km/h']>0]['Wind Speed (km/h)']
#
#directions = np.array(['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW',
#                       'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N'])
#
#data=data.dropna()
#data['Wind Direction (compass)'] = data['Wind Direction (degree)'].apply(
#        lambda x: directions[round(x/22.5)])
#
#data.to_csv("24h.csv")
