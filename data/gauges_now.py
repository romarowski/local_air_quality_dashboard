def values(limits):
    CO = limits[limits["Pollutant"]=='CO (mg/m³)']['Values'].iloc[0]
    NO2 = limits[limits["Pollutant"]=='NO₂ (µg/m³ )']['Values'].iloc[0]
    SO2 = limits[limits["Pollutant"]=='SO₂ (µg/m³)']['Values'].iloc[0]
    O3 = limits[limits["Pollutant"]=='O₃ (µg/m³ )']['Values'].iloc[0]
    PM25 = limits[limits["Pollutant"]=='PM₂.₅ (µg/m³ )']['Values'].iloc[0]
    PM10 = limits[limits["Pollutant"]=='PM₁₀ (µg/m³)']['Values'].iloc[0]
    
    vals = {'CO': CO, 'NO2': NO2, 'SO2': SO2, 'O3': O3, 'PM25': PM25,
        'PM10': PM10}
    return vals
