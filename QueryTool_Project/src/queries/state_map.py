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
    "o_state"   : "os",
    "d_state"   : "ds",
    "dms_orig"  : "do",
    "dms_dest"  : "dd",
    "mode"      : "m",
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

state = {
    "dms_orig" :[
                    f"{abv['o_state']}.description AS Domestic_Origin",
                    f"JOIN o_state {abv['o_state']} ON dms_orig = {abv['o_state']}.code",
                ],
    "dms_dest" :[
                    f"{abv['d_state']}.description AS Domestic_Destination", 
                    f"JOIN d_state {abv['d_state']} ON dms_dest = {abv['d_state']}.code",
                ],
    "sctg2"    :[
                    f"{abv['sctg']}.description AS Commodity",             
                    f"JOIN {abv['sctg']} ON sctg2 = {abv['sctg']}.code",
                ],
    "dms_mode" :[
                    f"{abv['mode']}.description AS Transportation",        
                    f"JOIN {abv['mode']} ON dms_mode = {abv['mode']}.code",
                ],
}

state2 = {
    "fr_orig"  :[
                    f"{abv['fr_orig']}.description AS Foreign_Origin",   
                    f"JOIN {abv['fr_orig']} ON fr_orig = {abv['fr_orig']}.code",
                ],
    "fr_inmode":[
                    f"{abv['fr_inmode']}.description AS Foreign_Transport",
                    f"JOIN {abv['fr_inmode']} ON fr_inmode = {abv['fr_inmode']}.code",
                ],
}

state3 = {
    "fr_dest"   :[
                    f"{abv['fr_dest']}.description AS Foreign_Destination",    
                    f"JOIN {abv['fr_dest']} ON fr_dest = {abv['fr_dest']}.code",
                 ],
    "fr_outmode":[
                    f"{abv['fr_outmode']}.description AS Foreign_Transportation",
                    f"JOIN {abv['fr_outmode']} ON fr_outmode = {abv['fr_outmode']}.code",
                 ],
}

tons = {
    "1997":"tons_1997",
    "2002":"tons_2002",
    "2007":"tons_2007",
    "2012":"tons_2012",
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
    "1997":"value_1997",
    "2002":"value_2002",
    "2007":"value_2007",
    "2012":"value_2012",
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
    "1997":"current_value_1997",
    "2002":"current_value_2002",
    "2007":"current_value_2007",
    "2012":"current_value_2012",
    "2017":"current_value_2017",
    "2018":"current_value_2018",
    "2019":"current_value_2019",
    "2020":"current_value_2020",
    "2021":"current_value_2021",
    "2022":"current_value_2022",
}

tmiles = {
    "1997":"tmiles_1997",
    "2002":"tmiles_2002",
    "2007":"tmiles_2007",
    "2012":"tmiles_2012",
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
