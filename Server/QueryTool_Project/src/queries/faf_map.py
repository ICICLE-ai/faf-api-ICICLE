abv = {
    "faf0"      : "f0",
    "faf1"      : "f1",
    "faf2"      : "f2",
    "state0"    : "s0",
    "state1"    : "s1",
    "state2"    : "s2",
    "o_faf"     : "of",
    "d_faf"     : "df",
    "sctg"      : "c",
    "dms_mode"  : "dm",
    "dist_band" : "db",
    "fr_orig"   : "fo",
    "fr_inmode" : "fim",
    "fr_dest"   : "fd",
    "fr_outmode": "fom",
}
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
faf = {
    "dms_orig" :[
                    f"{abv['o_faf']}.description AS Domestic_Origin",    
                    f"JOIN o_faf {abv['o_faf']} ON dms_orig = {abv['o_faf']}.code",
                ],
    "dms_dest" :[
                    f"{abv['d_faf']}.description AS Domestic_Destination",
                    f"JOIN d_faf {abv['d_faf']} ON dms_dest = {abv['d_faf']}.code",
                ],
    "sctg2"    :[
                    f"{abv['sctg']}.description AS Commodity",             
                    f"JOIN c ON {abv['sctg']} = {abv['sctg']}.code",
                ],
    "dms_mode" :[   
                    f"{abv['dms_mode']}.description AS Transportation",
                    f"JOIN {abv['dms_mode']} ON dms_mode = {abv['dms_mode']}.code",
                ],
    "dist_band":[
                    f"{abv['dist_band']}.description AS Distance",
                    f"JOIN {abv['dist_band']} ON dist_band = {abv['dist_band']}.code",
                ],
}
faf2 = {
    "fr_orig"  :[
                    "{abv['fr_orig']}.description AS Origin",
                    "JOIN {abv['fr_orig']} ON fr_orig = {abv['fr_orig']}.code",
                ],
    "fr_inmode":[
                    "{abv['fr_inmode']}.description AS Foreign_Transport",
                    "JOIN {abv['fr_inmode']} ON fr_inmode = {abv['fr_inmode']}.code"
                ],
}
faf3 = {
    "fr_dest"   :[
                    "fd.description AS Foreign_Destination",
                    "JOIN fd ON fr_dest = fd.code",
                 ],
    "fr_outmode":[
                    "{abv['fr_outmode']}.description AS Foreign_Transportation",
                    "JOIN {abv['fr_outmode']} ON fr_outmode = {abv['fr_outmode']}.code",
                 ],
}


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
