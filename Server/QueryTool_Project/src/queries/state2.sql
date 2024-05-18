SELECT 
	
    f0.index,
    os.description AS Origin,
    ds.description AS Destination,
    c.description As Commodity,
    m.description AS Transportation,
    fo.description AS Foreign_Origin,
    fom.description AS Foreign_Trans,
    
    tons_1997, tons_2002, tons_2007, tons_2012, tons_2017, tons_2018, tons_2019, tons_2020, tons_2021, 
    tons_2022, tons_2023, tons_2025, tons_2030, tons_2035, tons_2040, tons_2045, tons_2050,
    
    value_1997, value_2002, value_2007, value_2012, value_2017, value_2018, value_2019, value_2020, value_2021, 
    value_2022, value_2023, value_2025, value_2030, value_2035, value_2040, value_2045, value_2050,
    
    current_value_1997, current_value_2002, current_value_2007, current_value_2012, current_value_2017, current_value_2018, 
    current_value_2019, current_value_2020, current_value_2021, current_value_2022,
    
    tmiles_1997, tmiles_2002, tmiles_2007, tmiles_2012, tmiles_2017, tmiles_2018, tmiles_2019, tmiles_2020, tmiles_2021, 
    tmiles_2022, tmiles_2023, tmiles_2025, tmiles_2030, tmiles_2035, tmiles_2040, tmiles_2045, tmiles_2050,
    
    tons_2023_high, tons_2025_high, tons_2030_high, tons_2035_high, tons_2040_high, tons_2045_high, tons_2050_high, 
    tons_2023_low, tons_2025_low, tons_2030_low, tons_2035_low, tons_2040_low, tons_2045_low, tons_2050_low,
    
    value_2023_high, value_2025_high, value_2030_high, value_2035_high, value_2040_high, value_2045_high, value_2050_high, 
    value_2023_low, value_2025_low, value_2030_low, value_2035_low, value_2040_low, value_2045_low, value_2050_low

FROM _faf551_state_2 f0
JOIN c ON sctg2 = c.code
JOIN m ON dms_mode = m.code
JOIN o_state os ON dms_orig = os.code
JOIN d_state ds ON dms_dest = ds.code

JOIN fo ON fr_orig = fo.code
JOIN fom ON fr_inmode = fom.code;
