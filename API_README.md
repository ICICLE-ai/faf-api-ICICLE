#API Endpoint Description
This area will cover each endpoint in detail, including what it does, where the files are located, and the flow of the data points. After this, any interesting information from the databases will be shared below.

Starting at the root of the server in QueryTool_Project:
```
urls.py -> Rest_API/urls.py
views.py -> Rest_API/urls.py
classes being used for query develompent -> src/
lookup Tables -> src/tables
```
##get_table_data/
This endpoint queries the FAF database and retrieves one of six fully populated tables: faf0, faf1, faf2, faf3, state0, state1, state2, or state3 based on the timeframe given. Subsequently, the server generates a query to join these smaller tables with the main data tables and processes this query. The resulting data is stored in a Pandas DataFrame, converted to a CSV file, and provided to the user as a downloadable file. The file is named according to the selected table. If the user inputs incorrect information, an error message is returned detailing the issue.
``` python3
urls.py -> views.py -> GrabTable.py -> views.py -> Data_Lookup.py -> views.py -> User
#GatherAll Class in views controls this endpoint
```
The get_table_data endpoint uses GrabTable.py to build the query before sending it to Data_Lookup.py, which accesses the MySQL database and converts data into a pandas data frame. From here, the data is sent back to the user.

##point_to_point/
This endpoint takes in a specific commodity, or writing "all" gives all the commodities traded between two areas. This endpoint works for the FAF and state databases and will return the value and quantity per ton of the resource traded between the origin and destination based on year or timeframe if given two years. This endpoint also returns the method of transportation, and if either the origin or destination is foreign, it returns the foreign transit and any other states the commodity moved to before the final destination."

##domestic_exports/

##domestic_imports/

##importexport_sum/

##commodity_total/

