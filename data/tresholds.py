import pdb
from data import replace_name
from datetime import datetime
def count(df, df8, df24, limits, station="Privet Aviation"):
    data = {}
    df = df[df["Station"]==station]
    df8 = df8[df8["Station"]==station]
    df24 = df24[df24["Station"]==station]
  
    for pollutant in limits['Pollutant']:
        name = replace_name.replace(pollutant)
        if limits[limits['Pollutant']==pollutant]['Averaging time [h]'].iloc[0]==24:
            data[name] = df24[df24[pollutant]>\
                    limits[limits['Pollutant']==pollutant]['Limits'].iloc[0]].\
                    shape[0]
        elif limits[limits['Pollutant']==pollutant]['Averaging time [h]'].iloc[0]==8:
            data[name] = df8[df8[pollutant]>\
                    limits[limits['Pollutant']==pollutant]['Limits'].iloc[0]].\
                    shape[0]
        else: 
            data[name] = df[df[pollutant]>\
                    limits[limits['Pollutant']==pollutant]['Limits'].iloc[0]].\
                    shape[0]
        
    
    return data
