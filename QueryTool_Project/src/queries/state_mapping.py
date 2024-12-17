#state

state0 = {
    "dms_orig" : ["os.description AS Domestic_Origin",    "JOIN o_state os ON dms_orig = os.code"],
    "dms_dest" : ["ds.description AS Domestic_Destination", "JOIN d_state ds ON dms_dest = ds.code"],
    "sctg2"    : ["c.description AS Commodity",             "JOIN c ON sctg2 = c.code"],
    "dms_mode" : ["m.description AS Transportation",        "JOIN m ON dms_mode = m.code"],
}

state2 = {
    "fr_orig"  : ["fo.description AS Foreign_Origin",   "JOIN fo ON fr_orig = fo.code"],
    "fr_inmode": ["fom.description AS Transportation","JOIN fom ON fr_inmode = fom.code"],
}

state3 = {
    "fr_dest"   :["fd.description AS Foreign_Destination",    "JOIN fd ON fr_dest = fd.code"],
    "fr_outmode":["fdm.description AS Transportation","JOIN fdm ON fr_outmode = fdm.code"],
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

tons_sum = {
    "1997":"SUM(tons_1997) AS '1997'",
    "2002":"SUM(tons_2002) AS '2002'",
    "2007":"SUM(tons_2007) AS '2007'",
    "2012":"SUM(tons_2012) AS '2012'",
    "2017":"SUM(tons_2017) AS '2017'",
    "2018":"SUM(tons_2018) AS '2018'",
    "2019":"SUM(tons_2019) AS '2019'",
    "2020":"SUM(tons_2020) AS '2020'",
    "2021":"SUM(tons_2021) AS '2021'",
    "2022":"SUM(tons_2022) AS '2022'",
    "2023":"SUM(tons_2023) AS '2023'",
    "2025":"SUM(tons_2025) AS '2025'",
    "2030":"SUM(tons_2030) AS '2030'",
    "2035":"SUM(tons_2035) AS '2035'",
    "2040":"SUM(tons_2040) AS '2040'",
    "2045":"SUM(tons_2045) AS '2045'",
    "2050":"SUM(tons_2050) AS '2050'",
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

value_sum = {
    "1997":"SUM(value_1997)  AS Total_Value_1997",
    "2002":"SUM(value_2002)  AS Total_Value_2002",
    "2007":"SUM(value_2007)  AS Total_Value_2007",
    "2012":"SUM(value_2012)  AS Total_Value_2012",
    "2017":"SUM(value_2017)  AS Total_Value_2017",
    "2018":"SUM(value_2018)  AS Total_Value_2018",
    "2019":"SUM(value_2019)  AS Total_Value_2019",
    "2020":"SUM(value_2020)  AS Total_Value_2020",
    "2021":"SUM(value_2021)  AS Total_Value_2021",
    "2022":"SUM(value_2022)  AS Total_Value_2022",
    "2023":"SUM(value_2023)  AS Total_Value_2023",
    "2025":"SUM(value_2025)  AS Total_Value_2025",
    "2030":"SUM(value_2030)  AS Total_Value_2030",
    "2035":"SUM(value_2035)  AS Total_Value_2035",
    "2040":"SUM(value_2040)  AS Total_Value_2040",
    "2045":"SUM(value_2045)  AS Total_Value_2045",
    "2050":"SUM(value_2050)  AS Total_Value_2050",
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

