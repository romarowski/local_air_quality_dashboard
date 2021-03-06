import pandas as pd

data = {'Label': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        'Device ID': ['SEN01P0001', 'SEN01P0002', 'SEN01P0002', 'SEN01P0003',
            'SEN01P0004', 'SEN01P0005','SEN01P0006', 'SEN01P0007','SEN01P0008',
            'SEN02P0002', 'SEN02P0001', 'SEN02P0005','SEN02P0004'],
        'Device Name': ['Privet Aviation', 'Primary Runway', 'ATC Tower',
            'Royal Terminal', 'Air Cargo', 'Secondary Runway 01', 
            'Secondary Runway 02', 'Fire Station', 'CS 59 Storage',
            'AE123 Inbound K.S.R', 'Family Camp', 'SASCO Station 3',
            'RYADH FRONT (SASCO STATION 1)'],
        'Latitude': [24.9655448, 24.963136, 24.9560084, 24.95376, 24.976318,
            24.956003, 24.941005, 24.963901, 24.938702, 24.854928, 24.941528,
            24.890091, 24.844891],
        'Longitude': [46.722919, 46.712787, 46.697312, 46.695125, 46.694, 
            46.682273, 46.691696, 46.685287, 46.739647, 46.681631, 46.649335,
            46.693224, 46.732690],
        'Measured Variables': 
        ['''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3, Wind direction,
         Wind speed''',
         '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''',
        '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''',
        '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''',
        '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''',
        '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''',
        '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''',
        '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''',
        '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''',
        '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''',
        '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''',
        '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''',
        '''PM2.5, PM10,  PM1, CO2, Temperature, Humidity, Light, UV, 
         Leq, Lmax, Lmin, SO2, CO, H2S, NO, NO2, O3''']
        }

data = pd.DataFrame.from_dict(data)  
