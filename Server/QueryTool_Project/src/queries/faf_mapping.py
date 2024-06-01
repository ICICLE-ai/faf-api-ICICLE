#faf

faf0 = {
    "dms_orig" : ["of0.description AS Domestic_Origion",    "JOIN o_faf of0 ON dms_orig = of0.code"],
    "dms_dest" : ["df.description AS Domestic_Destination", "JOIN d_faf df  ON dms_dest = df.code"],
    "sctg2"    : ["c.description AS Commodity",             "JOIN c ON sctg2 = c.code"],
    "dms_mode" : ["m.description AS Transportation",        "JOIN m ON dms_mode = m.code"],
    "dist_band": ["db.description AS Distance",             "JOIN db ON dist_band = db.code"],
}

faf2 = {
    "fr_orig"  : ["fo.description AS Origion",           "JOIN fo ON fr_orig = fo.code"],
    "fr_inmode": ["fom.description AS Foreign_Transport","JOIN fom ON fr_inmode = fom.code"],
}

faf3 = {
    "fr_dest"   :["fd.description AS Foreign_Destination",    "JOIN fd ON fr_dest = fd.code"],
    "fr_outmode":["fdm.description AS Foreign_Transportation","JOIN fdm ON fr_outmode = fdm.code"],
}

faf0_column_names = [
"Domestic_Origion", "Domestic_Destination", "Commodity", "Domestic_Transportation", "Distance","tons_2017", "tons_2018", "tons_2019", "tons_2020", "tons_2021", "tons_2022", "tons_2023", "tons_2025", "tons_2030", "tons_2035", "tons_2040", "tons_2045", "tons_2050", "value_2017", "value_2018", "value_2019", "value_2020", "value_2021", "value_2022", "value_2023", "value_2025", "value_2030", "value_2035", "value_2040", "value_2045", "value_2050", "current_value_2017", "current_value_2018", "current_value_2019", "current_value_2020", "current_value_2021", "current_value_2022", "tmiles_2017", "tmiles_2018", "tmiles_2019", "tmiles_2020", "tmiles_2021", "tmiles_2022", "tmiles_2023", "tmiles_2025", "tmiles_2030", "tmiles_2035", "tmiles_2040", "tmiles_2045", "tmiles_2050", "tons_2023_high", "tons_2025_high", "tons_2030_high", "tons_2035_high", "tons_2040_high", "tons_2045_high", "tons_2050_high", "tons_2023_low", "tons_2025_low", "tons_2030_low", "tons_2035_low", "tons_2040_low", "tons_2045_low", "tons_2050_low", "value_2023_high", "value_2025_high", "value_2030_high", "value_2035_high", "value_2040_high", "value_2045_high", "value_2050_high", "value_2023_low", "value_2025_low", "value_2030_low", "value_2035_low", "value_2040_low", "value_2045_low", "value_2050_low"
]
faf2_column_names = [
"Foreign_Origin","Domestic_Origion", "Domestic_Destination", "Commodity", "Foreign_Transportation", "Domestic_Transportation", "Distance","tons_2017", "tons_2018", "tons_2019", "tons_2020", "tons_2021", "tons_2022", "tons_2023", "tons_2025", "tons_2030", "tons_2035", "tons_2040", "tons_2045", "tons_2050", "value_2017", "value_2018", "value_2019", "value_2020", "value_2021", "value_2022", "value_2023", "value_2025", "value_2030", "value_2035", "value_2040", "value_2045", "value_2050", "current_value_2017", "current_value_2018", "current_value_2019", "current_value_2020", "current_value_2021", "current_value_2022", "tmiles_2017", "tmiles_2018", "tmiles_2019", "tmiles_2020", "tmiles_2021", "tmiles_2022", "tmiles_2023", "tmiles_2025", "tmiles_2030", "tmiles_2035", "tmiles_2040", "tmiles_2045", "tmiles_2050", "tons_2023_high", "tons_2025_high", "tons_2030_high", "tons_2035_high", "tons_2040_high", "tons_2045_high", "tons_2050_high", "tons_2023_low", "tons_2025_low", "tons_2030_low", "tons_2035_low", "tons_2040_low", "tons_2045_low", "tons_2050_low", "value_2023_high", "value_2025_high", "value_2030_high", "value_2035_high", "value_2040_high", "value_2045_high", "value_2050_high", "value_2023_low", "value_2025_low", "value_2030_low", "value_2035_low", "value_2040_low", "value_2045_low", "value_2050_low"
]
faf3_column_names = [
"Domestic_Origion", "Domestic_Destination", "Foreign_Destination", "Commodity", "Domestic_Transportation", "Foreign_Transportation", "Distance","tons_2017", "tons_2018", "tons_2019", "tons_2020", "tons_2021", "tons_2022", "tons_2023", "tons_2025", "tons_2030", "tons_2035", "tons_2040", "tons_2045", "tons_2050", "value_2017", "value_2018", "value_2019", "value_2020", "value_2021", "value_2022", "value_2023", "value_2025", "value_2030", "value_2035", "value_2040", "value_2045", "value_2050", "current_value_2017", "current_value_2018", "current_value_2019", "current_value_2020", "current_value_2021", "current_value_2022", "tmiles_2017", "tmiles_2018", "tmiles_2019", "tmiles_2020", "tmiles_2021", "tmiles_2022", "tmiles_2023", "tmiles_2025", "tmiles_2030", "tmiles_2035", "tmiles_2040", "tmiles_2045", "tmiles_2050", "tons_2023_high", "tons_2025_high", "tons_2030_high", "tons_2035_high", "tons_2040_high", "tons_2045_high", "tons_2050_high", "tons_2023_low", "tons_2025_low", "tons_2030_low", "tons_2035_low", "tons_2040_low", "tons_2045_low", "tons_2050_low", "value_2023_high", "value_2025_high", "value_2030_high", "value_2035_high", "value_2040_high", "value_2045_high", "value_2050_high", "value_2023_low", "value_2025_low", "value_2030_low", "value_2035_low", "value_2040_low", "value_2045_low", "value_2050_low"
]
table = {
    "faf0":"_faf551_faf_0",
    "faf1":"_faf551_faf_1",
    "faf2":"_faf551_faf_2",
    "faf3":"_faf551_faf_3",
    "state0":"_faf551_state_0",
    "state1":"_faf551_state_1",
    "state2":"_faf551_state_2",
    "state3":"_faf551_state_3",
}

tons = {
    "2017":"tons_2017",
    "2018":"tons_2018",
    "2019":"tons_2019",
    "2020":"tons_2020",
    "2021":"tons_2021",
    "2022":"tons_2022",
    "2023":"tons_2023",
    "2025":"tons_2025",
    "2030":"tons_2030",
    "2035":"tons_2035",
    "2040":"tons_2040",
    "2045":"tons_2045",
    "2050":"tons_2050",
}

value = {
    "2017":"value_2017",
    "2018":"value_2018",
    "2019":"value_2019",
    "2020":"value_2020",
    "2021":"value_2021",
    "2022":"value_2022",
    "2023":"value_2023",
    "2025":"value_2025",
    "2030":"value_2030",
    "2035":"value_2035",
    "2040":"value_2040",
    "2045":"value_2045",
    "2050":"value_2050",
}

current_value = {
    "2017":"current_value_2017",
    "2018":"current_value_2018",
    "2019":"current_value_2019",
    "2020":"current_value_2020",
    "2021":"current_value_2021",
    "2022":"current_value_2022",
}

tmiles = {
    "2017":"tmiles_2017",
    "2018":"tmiles_2018",
    "2019":"tmiles_2019",
    "2020":"tmiles_2020",
    "2021":"tmiles_2021",
    "2022":"tmiles_2022",
    "2023":"tmiles_2023",
    "2025":"tmiles_2025",
    "2030":"tmiles_2030",
    "2035":"tmiles_2035",
    "2040":"tmiles_2040",
    "2045":"tmiles_2045",
    "2050":"tmiles_2050",
}

tons_high = {
    "2023":"tons_2023_high",
    "2025":"tons_2025_high",
    "2030":"tons_2030_high",
    "2035":"tons_2035_high",
    "2040":"tons_2040_high",
    "2045":"tons_2045_high",
    "2050":"tons_2050_high",
}

tons_low = {
    "2023":"tons_2023_low",
    "2025":"tons_2025_low",
    "2030":"tons_2030_low",
    "2035":"tons_2035_low",
    "2040":"tons_2040_low",
    "2045":"tons_2045_low",
    "2050":"tons_2050_low",
}

value_high = {
    "2023":"value_2023_high",
    "2025":"value_2025_high",
    "2030":"value_2030_high",
    "2035":"value_2035_high",
    "2040":"value_2040_high",
    "2045":"value_2045_high",
    "2050":"value_2050_high",
}

value_low = {
    "2023":"value_2023_low",
    "2025":"value_2025_low",
    "2030":"value_2030_low",
    "2035":"value_2035_low",
    "2040":"value_2040_low",
    "2045":"value_2045_low",
    "2050":"value_2050_low",
}

