# API Endpoint Description
**Version: 0.1.0**

This API is designed to retrieve information from the Freight Analysis Framework (FAF) dataset, which was created by the Federal Highway Administration (FHWA) to illustrate freight movement in the United States.

The following section provides a detailed overview of each endpoint, including the required input parameters, the data returned, and a description of the endpoint's functionality. Each endpoint is accompanied by an example demonstrating the expected format of the input data. All POST request bodies must be formatted as **JSON**. For GET requests, parameters should be passed as query strings.

# Endpoints

* [get_table_data](#get_table_data)      
* [point_to_point](#point_to_point)
* [exports_imports_details](#exports_imports_details)  
* [import_export_sum](#import_export_sum)
* [commodity_total](#commodity_total) 
* [data_option](#data_option)


## get_table_data/
This endpoint queries the FAF database and retrieves one of six fully populated tables: faf0, faf1, faf2, faf3, state0, state1, state2, or state3 based on the timeframe given. Subsequently, the server generates a query to join these smaller tables with the main data tables and processes this query. The resulting data is stored in a Pandas DataFrame, converted to a CSV file, and provided to the user as a downloadable file. The file is named according to the selected table. If the user inputs incorrect information, an error message is returned detailing the issue.

### attributes:
* table(string): name of which table to desired to get information from
* timeframe(list of int): can either be a single year, or a range between two years

### return:
returns a csv file that can be downloaded.
    
``` python
#example data input
tableModel_example = {
    "table"    : "faf0",
    "timeframe":[2013, 2018],
}
```
The get_table_data endpoint uses GrabTable.py to build the query before sending it to Data_Lookup.py, which accesses the MySQL database and converts data into a CSV file. From here, the data is sent back to the user.

## point_to_point/
This endpoint takes in a specific commodity, or writing "all" gives all the commodities traded between two areas. This endpoint works for the FAF and state databases and will return the value and quantity per ton of the resource traded between the origin and destination based on year or timeframe if given two years. This endpoint also returns the method of transportation, and if either the origin or destination is foreign, it returns the foreign transit and any other states the commodity moved to before the final destination."

### attributes:
* commodity(str): Can either be any of the commodity options or 'all' to return all of the trades from origin to destination
* origin(str): Beginning location 
* destination(str): Second location 
* timeframe(list of int): can either be a single year, or a range between two years

### return:
returns a csv file that can be downloaded.

``` python
#example data input
pointToPointExample = {
    "commodity"  :"all",
    "origin"     :"Alaska",
    "destination":"California",
    "timeframe"  :[2017, 2021],
}
```
From here on out, the classes in views and the classes in src are names roughly the same for simplicity when trying to find what connects to what. If they are named the exact same, the endpoints can fail.

## domestic_exports/
This endpoint takes in a region or state with a year or year frame and returns all exported commodities from that area. This only applies to domestic-based trade. The endpoint returns the commodity type, the transportation type, the area the commodity was sent to, and the year's ton and value.

### attributess:
* origin(str): Specific location being used
* timeframe(list of int): can either be a single year, or a range between two years

### return:
returns a csv file that can be downloaded.

``` python
#example data input
exportSingleExample = {
    "origin"   :"Indiana",
    "timeframe":[2018,2025],
}
```

## exports_imports_details/
This endpoint takes in a region or state with a year or year frame and returns all imported commodities from that area. This only applies to domestic-based trade. The endpoint returns the commodity type, the transportation type, the area the commodity was sent to, and the year's ton and value.

### attributes:
* origin(str): Specific location being used
* timeframe(list of int): can either be a single year, or a range between two years (e.g., [2017], [2017,2025])
* commodity (str): Type of good being transported (e.g., "Coal")   
* destination (str): Specific location goods are being sent to  
* transpotation (str): Mode of transport used (e.g., "Truck", "Rail", "Water")  
* flow (str): Nature of the shipment (e.g., "domestic", "foreign-Import", "foreign-Export")  

### return:
returns a csv file that can be downloaded.

``` python
#example data input
exports_imports_details_Example ={
  "origin": "Indiana",
  "commodity": "Animal feed",
  "destination": "Alaska",
  "transpotation": "Truck",
  "flow": "domestic",
  "timeframe": [
    2018,
    2025
  ]
}
```

## import_export_sum/
This endpoint takes in an origin named and a year/year frame and calculates the sum of each resource imported and exported from the said area. It returns data by giving the area’s name, the resource, whether it was imported or exported, and the summation of said resource based on year. Currently, this only works for domestic imports and outports.

### attributes:
* origin(str): Specific location being used
* timeframe(list of int): can either be a single year, or a range between two years (e.g., [2017], [2017,2025]) 
* destination (str): Specific location goods are being sent to
* flow (str): Nature of the shipment (e.g., "domestic", "foreign-Import", "foreign-Export")  

### return:
returns a csv file that can be downloaded.

``` python
#example data input
imp_exp_Example = {
  "origin": "Indiana",
  "timeframe": [
    2017,
    2020
  ],
  "destination": "",
  "flow": "domestic"
}
```

Both the Imports.py and Exports.py are used in this endpoint. The manipulations to build the output csv file are found in the RawResources class located in views.

## commodity_total/
Takes the commodities in each state and adds up their total based on import, export or both and sorts the return based on ton amount. The time frame is based on year or year frame, and the return will give the location of the ranked commodity and if it was imported or exported

### attributes:
* timeframe(list of int): can either be a single year, or a range between two years
* option(str): state or faf, used to gather information from either the faf tables or the state tables

### return:
returns a csv file that can be downloaded.

``` python
#example data input
commExample = {
        "timeframe":[2017, 2020],
        "option": "region",
}
```
## data_option/
The dataset provides a predefined set of options for certain tables in the FAF dataset. For instance, the 'state' table includes 50 states. This endpoint returns all possible data choices for the specified option value within the given field.
### attributes:
* option(str): choices are 'states', 'regions, 'commodities, 'foreign'

### return:
Returns all supported data points from the dataset in JSON format matching the option.
``` python
#example data input
Example = {
        "option": "regions",
}
```

# Server Finds
## Importing vs Exporting
The main six tables have some form of origin and destination. Using this, importing would consist of trade from destination to origin, and exporting would be trade from origin to destination.

## Time Organized
Time frames are organized by year and can be found in the columns. Each new year brings another order of columns, such as ton_2022 and value_2022. Anything in the future is estimated
and subjected to change. Each recent year has additional columns for the highs and lows of each year that give room for error, unlike older years

## Directional Flow Numbers
Any table with a 2 relates to imports coming into the U.S, and any table with a 3 relates to exports leaving the U.S. 1 refers to goods traded within the borders of the U.S., and 0 includes everything from 1, but it also consists of the movement of goods from 2 and 3 inside the U.S., but before/after leaving the U.S.

# Ideas for Further Development

## Table Transitivity
There was a proposal to extend the import and export endpoints to include products traded in and out of the U.S., but feasibility is still under evaluation. Current understanding suggests that tables labeled with "1" do not share data with those marked "2" and "3," although this needs formal confirmation to avoid data duplication in queries. If establishing transitivity between the tables labeled "1," "2," and "3" is not feasible, separate endpoints may be created for goods exported from and imported into the U.S. Additionally, it is noted that no transitivity is expected between the FAF and state tables, only among FAF1, FAF2, FAF3, and STATE1, STATE2, and STATE3.

## JSON Sent for Small Queries
One proposed idea is to use JSON format for transmitting data when the volume is relatively small. JSON is the standard data format for RESTful APIs and is highly compatible with most programming languages. Its flexibility makes it particularly suitable for small datasets due to its ability to handle hierarchical structures, preserve data types, and support nested relationships. Furthermore, JSON's human-readable format and wide compatibility with various libraries and languages enhance its effectiveness for data interchange. Given these advantages, incorporating JSON as an option for transmitting smaller data quantities would be beneficial.

# Versioning
### V0.1.0
This marks the release of the first full version of the API, introducing the following endpoints: `data_option`, `domestic_exports`, `domestic_imports`, `get_table_data`, `import_export_sum`, and `point_to_point`.
