# FAF-API Server

## A django server designed to give users and API that delivers information about the FAF dataset

This server was designed to access a MySQL server and access the FAF database which is done in the Data_Lookup file stored in the src folder in the root of the server. From there, the value was delivered through endpoints located in the urls.py and views.py files which can be found in the Rest_API app. These endpoints access classes stored in the base of the src directory that build queries to be sent to the database using the faf_mapping.py and state_mapping.py files. This method of querying the FAF database was done to:

*Prevent users from having access to the database directly to prevent overwriting and manipulating the database
*Allow for future editing when new data is added by altering the lookup tables instead of the physical query which would be done with automation in future development

Data -> urls -> views -> src/classes -> Data_Lookup -> MySQL -> view -> sent to user

## Starting Up the Server
Currently the server is not containerized, so the python envionment needs to be activated as it contains all of the needed installations for the server to run which can be found in lib/python3.8/site-packages in the Server directory.

1. Activate python environment by using "source bin/activate" in the server directory
2. Go to Server/QueryTool_Project/ directory
3. Run "python3 manage.py runserver" or if you want to run on a specific port "python3 manage.py runserver #.#.#.#:port_#"

This should start the server. To test, go to http://127.0.0.1:8000/api/schema/swagger-ui/#/where you should see the current endpoints.

## Working on the Project

