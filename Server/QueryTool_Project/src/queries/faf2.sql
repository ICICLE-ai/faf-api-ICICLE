SELECT 
	f0.index,
    fo.description as Origion,
    df.description as Destination,
    c.description as Commodity,
    fom.description as Foreign_Trans,
    m.description as Transportation,
    db.description as Distance,
    f0.tons_2017, f0.tons_2018, f0.tons_2019, f0.tons_2020, f0.tons_2021, f0.tons_2022, f0.tons_2023, 
    f0.tons_2025, f0.tons_2030, f0.tons_2035, f0.tons_2040, f0.tons_2045, f0.tons_2050,
    
    f0.value_2017, f0.value_2018, f0.value_2019, f0.value_2020, f0.value_2021, f0.value_2022, f0.value_2023, 
    f0.value_2025, f0.value_2030, f0.value_2035, f0.value_2040, f0.value_2045, f0.value_2050,
    
    f0.current_value_2017, f0.current_value_2018, f0.current_value_2019, f0.current_value_2020, f0.current_value_2021, 
    f0.current_value_2022, 
    
    f0.tmiles_2017, f0.tmiles_2018, f0.tmiles_2019, f0.tmiles_2020, f0.tmiles_2021, f0.tmiles_2022, f0.tmiles_2023, 
    f0.tmiles_2025, f0.tmiles_2030, f0.tmiles_2035, f0.tmiles_2040, f0.tmiles_2045, f0.tmiles_2050,
    
    f0.tons_2023_high, f0.tons_2025_high, f0.tons_2030_high, f0.tons_2035_high, f0.tons_2040_high, f0.tons_2045_high, f0.tons_2050_high,
    
    f0.tons_2023_low, f0.tons_2025_low, f0.tons_2030_low, f0.tons_2035_low, f0.tons_2040_low, f0.tons_2045_low, f0.tons_2050_low,
    
    f0.value_2023_high, f0.value_2025_high, f0.value_2030_high, f0.value_2035_high, f0.value_2040_high, 
    f0.value_2045_high, f0.value_2050_high,
    
    f0.value_2023_low, f0.value_2025_low, f0.value_2030_low, f0.value_2035_low, f0.value_2040_low, 
    f0.value_2045_low, f0.value_2050_low
    
    
    
FROM _faf551_faf_2 f0
JOIN fo ON f0.fr_orig = fo.code
JOIN o_faf of0 ON f0.dms_orig = of0.code
JOIN d_faf df  ON f0.dms_dest = df.code
JOIN m on f0.dms_mode = m.code
JOIN c on f0.sctg2 = c.code
JOIN fom on f0.fr_inmode = fom.code
JOIN db on f0.dist_band = db.code
JOIN db on f0.dist_band = db.code;
