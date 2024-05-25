tableModel_example = [
    {
        "table": "faf0",
    }
]

table_CSVExample = [["Origin", "Destination","Commodity", "Transportation","Distance","ton_2017","tons_2017", "tons_2018", "tons_2019", "tons_2020", "tons_2021", "tons_2022", "tons_2023","tons_2025", "tons_2030", "tons_2035", "tons_2040", "tons_2045", "tons_2050","value_2017", "value_2018", "value_2019", "value_2020", "value_2021", "value_2022", "value_2023","value_2025", "value_2030", "value_2035", "value_2040", "value_2045", "value_2050","current_value_2017", "current_value_2018", "current_value_2019", "current_value_2020", "current_value_2021","current_value_2022","tmiles_2017", "tmiles_2018", "tmiles_2019", "tmiles_2020", "tmiles_2021","tmiles_2022", "tmiles_2023","tmiles_2025", "tmiles_2030", "tmiles_2035", "tmiles_2040", "tmiles_2045", "tmiles_2050","tons_2023_high", "tons_2025_high", "tons_2030_high", "tons_2035_high", "tons_2040_high", "tons_2045_high", "tons_2050_high","tons_2023_low", "tons_2025_low", "tons_2030_low", "tons_2035_low", "tons_2040_low", "tons_2045_low", "tons_2050_low","value_2023_high", "value_2025_high", "value_2030_high", "value_2035_high", "value_2040_high","value_2045_high", "value_2050_high","value_2023_low", "value_2025_low", "value_2030_low", "value_2035_low", "value_2040_low","value_2045_low", "value_2050_low"]]

PointToPointExample1 = [
    {
        "commodity"  :"Live animals/fish",
        "origin"     :"Alabama",
        "destination":"Florida",
        "timeframe"  :[2023],
    }
]
PointToPointExample2 = [
    {
        "commodity"  :"all",
        "origin"     :"Alaska",
        "destination":"California",
        "timeframe"  :[2017, 2021],
    }
]
PtoPReturnExample = [
    {
        "commodity":"Logs",
        "ton"      :1.9478550000000001,
        "transport":"Truck",
        "year"     :2017,
    },      
    {
        "commodity":"Paper articles",
        "ton"      :3.8394749999999997,
        "transport":"Rail",
        "year"     :2017,
    },
    {
        "commodity":"Waste/scrap",
        "ton"      :0,
        "transport":"Truck",
        "year"     :2018,
    },
    {
        "commodity":"Logs",
        "ton"      :0.00052,
        "transport":"Truck",
        "year"     :2018,
    },

]
exportSingleExample1 = [
    {
        "origin"   :"Indiana",
        "timeframe":[2018],
    }
]
exportMultiExample2 = [
    {
        "origin":"Pennsylvania",
        "year"  :[2020, 2023],
    }
]
exportReturnExample = [
    {
        "destination":"Alabama",
        "commodity"  :"Logs",
        "ton"        :1.9478550000000001,
        "transport"  :"Truck",
        "year"       :2017,
    },      
    {
        "destination":"virgina",
        "commodity"  :"Paper articles",
        "ton"        :3.8394749999999997,
        "transport"  :"Rail",
        "year"       :2017,
    },
    {
        "destination":"New York",
        "commodity"  :"Waste/scrap",
        "ton"        :0,
        "transport"  :"Truck",
        "year"       :2018,
    },
    {
        "destination":"Florida",
        "commodity"  :"Logs",
        "ton"        :0.00052,
        "transport"  :"Truck",
        "year"       :2018,
    },
]
importReturnExample = [
    {
        "origin"   :"Alabama",
        "commodity":"Logs",
        "ton"      :1.9478550000000001,
        "transport":"Truck",
        "year"     :2017,
    },      
    {
        "origin"   :"virgina",
        "commodity":"Paper articles",
        "ton"      :3.8394749999999997,
        "transport":"Rail",
        "year"     :2017,
    },
    {
        "origin"   :"New York",
        "commodity":"Waste/scrap",
        "ton"      :0,
        "transport":"Truck",
        "year"     :2018,
    },
    {
        "origin"   :"Florida",
        "commodity":"Logs",
        "ton"      :0.00052,
        "transport":"Truck",
        "year"     :2018,
    },

]
rawExample1 = [
    {
        "origin"   :"Texas",
        "timeframe":[2017],
        "option"   :"Import",
    }
]
rawExample2 = [
    {
        "origin"   :"Texas",
        "timeframe":[2017, 2020],
        "option"   :"Both",
    }

]
rawExampleReturn = [
    {
        "commodity":"Logs",
        "ton"      :5721.232202,
        "option"   :"Export",
    }
]
commtotalExample1 = [
    {
        "commodity":"Logs",
        "timeframe":[2017],
        "option"   :"Export",
    }
]
commtotalExample2 = [
    {
        "commodity":"Logs",
        "timeframe":[2017,2020],
        "option"   :"Both",
    }
]

commtotalReturnExample = [
    {
        "origin":"Mississippi",
        "ton"   :72723.0121,
        "option":"Import",
    }
]
ratioExample1 = [
    {
        "origin"   :"Texas",
        "timeframe":[2017],
    }
]
ratioExample2 = [
    {
        "origin"   :"Texas",
        "timeframe":[2017, 2020],
    }
]
ratioReturnExample = [
    {
        "commodity":"Logs",
        "ratio":100.58339,
        "ton_import":72723.0121,
        "ton_export":723.0121,
    }
]
