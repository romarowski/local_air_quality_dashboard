from data import filter_dates
import pandas as pd
import pdb
def info(start_date, end_date, poll_df, station='Privet Aviation'):
    poll_df = filter_dates.filtered(start_date, end_date, poll_df)
    poll_df = poll_df[poll_df['Station']==station]
    #T_avg = poll_df['Temperature (°C)'].mean() 
    T_avg = 25
    T_avg += 273.15 #Kelvin
    molar_mass= {'CO': 28.01, #g/mol
                'NOtwo':  46,
                'SOtwo': 64.07,
                'Othree': 48,
                'HtwoS': 34.1,
                }
    p = 101325 #Pa
    R = 8.3145 #m^3 Pa K^-1 mol^-1
    limit = {'CO': 35, #ppm 
             'NOtwo': 100, #ppb 
             'SOtwo': 75, #ppb 
             'Othree': .07, #ppm 
             'HtwoS': .1 # ppm TBC if this US correct
             }
    sa_limit = {'CO': 32, #ppm
                'NOtwo': 350, #ppb
                'SOtwo': 280, #ppb
                'Othree': .08, #ppm
                'HtwoS': .1 #ppm 
                }
    dict_limits = {'Pollutant':['CO (mg/m³)', 'NO₂ (µg/m³ )', 'SO₂ (µg/m³)',
        'O₃ (µg/m³ )', 'H₂S (µg/m³ )', 'PM₂.₅ (µg/m³ )', 'PM₁₀ (µg/m³)'],
                   'Averaging time [h]':[1,1,1,8,24,24,24]}
    limit_us = []    
    limit_sa = []
    
    for pollutant in molar_mass:
        limit_density = limit[pollutant]*molar_mass[pollutant]*p / \
                                  (R *  T_avg * 1e6)
        if pollutant == 'Othree' or pollutant =='HtwoS':
            limit_density *= 1e3
        limit_density *= 1e3
        limit_us.append(round(limit_density))

        limit_density_sa = sa_limit[pollutant]*molar_mass[pollutant]*p / \
                                  (R *  T_avg * 1e6)
        if pollutant == 'Othree' or pollutant == 'HtwoS':
            limit_density_sa *= 1e3
        limit_density_sa *= 1e3
        limit_sa.append(round(limit_density_sa))
    limit_sa.extend((35, 340))
    limit_us.extend((35, 150))
    dict_limits['US Limits'] = limit_us
    dict_limits['SA Limits'] = limit_sa
    df = pd.DataFrame.from_dict(dict_limits)
    #pdb.set_trace()
    df['Values'] = poll_df[df['Pollutant'].to_numpy()].mean().to_numpy()

    return df

