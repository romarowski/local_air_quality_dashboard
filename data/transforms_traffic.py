import os
import pandas as pd
import numpy as np
from data import get_weekly_flight_trend
import datetime as dt
import pdb
#traffic_df = pd.read_excel(r"data/traffic_input_data/AODB_MAY_2020.xlsx") 

#pctge_flights_per_terminal = traffic_df['Air Terminal'].value_counts(normalize=True) * 100
#
##Prepare dataset for weekly trend
#
#flights_by_date = pd.DataFrame(traffic_df['ETAD'])
#flights_by_date['To Date'] = pd.to_datetime(flights_by_date['ETAD'])
#count_weekly_flights = flights_by_date.groupby(flights_by_date['To Date'].dt.isocalendar().week).count()
#count_weekly_flights = np.array(count_weekly_flights['To Date'])
#
#
#button_format = get_weekly_flight_trend.button_format(count_weekly_flights)

data = pd.read_csv('data/traffic_input_data/traffic.csv')
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
data_weekly = pd.read_csv('data/traffic_input_data/traffic.csv')

data_weekly['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

data_weekly['Date'] = data_weekly['Date'] - pd.to_timedelta(7, unit='d')
data_weekly = data_weekly.groupby(pd.Grouper(key='Date', freq='W-Mon'))['To Date']\
           .count()\
           .reset_index()\
           .sort_values('Date')\
           .rename(columns={'To Date': 'Operation Count'})

#THIS DOES NOTHING REMOVECalculating weekly traffic trends
max_year = max(data['Year'])
data_but = data[data['Year']==max_year]
data_but['Week nbr'] = data_but['Date'].apply(lambda x: x.isocalendar()[1])
count_weekly_flights = data_but.groupby(by='Week nbr').count().reset_index()
count_weekly_flights = np.array(count_weekly_flights['To Date'])
button_format = get_weekly_flight_trend.button_format(count_weekly_flights)

##################------------NEW GENERATE BIG DF-------------------#################

#input_data_df_list = []
#pollutant_name = []
#
#directory = r'data/traffic_input_data'
#input_files = os.listdir(directory)
##sep = ' 1 Hours Avg.csv' #Set separation for file_names
#
#for file_name in input_files:
#  #  station_name = file_name.split(sep, 1)[0]
#    file_dir = directory + '/' + file_name
#    df = pd.read_excel(file_dir)
# #   df = df.assign(Station = station_name)
#    input_data_df_list.append(df)
#
## Creates a huge df with all data
#data = pd.concat(input_data_df_list)
## Adds the month column
#data['To Date'] = pd.to_datetime(data['STAD'])
#
#data["Month"] = pd.DatetimeIndex(data["To Date"]).month_name()
#data["Month Index"] = pd.DatetimeIndex(data["To Date"]).month
#data["Day"] = pd.DatetimeIndex(data["To Date"]).day_name()
#data["Day Index"] = pd.DatetimeIndex(data["To Date"]).dayofweek
#data['Day of Month'] = pd.DatetimeIndex(data['To Date']).day
#data["Hour"] = pd.DatetimeIndex(data["To Date"]).hour
#data["Date"] = pd.DatetimeIndex(data["To Date"]).date
#
##data = data[['STAD', 'Runway']]
#data['Runway'] = data['Runway'].str.replace('-','')
#data['Runway'] = data['Runway'].str.replace('A','')
#data['Runway'] = data['Runway'].str.replace('D','')
#data=data.sort_values('To Date', ascending=False)
##data = data.dropna()
#data = data.drop(['Call Sign', 'Passenger Handling Agent', 'Ramp Handling Agent', 'Cargo Handling Agent', 'Maintenance Handling Agent'], axis='columns')
#
#
#
#
#
#data.to_csv('data/traffic_input_data/traffic.csv')

