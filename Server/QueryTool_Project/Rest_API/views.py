#Rest_API/views.py
from django.shortcuts import render
from django.http      import HttpResponse
import pandas as pd
from io import StringIO


from rest_framework.response   import Response
from rest_framework.decorators import api_view
from rest_framework.views      import APIView

from src.Data_Lookup  import QueryTool
from src.GrabTable    import GrabTable
from src.PointToPoint import PointToPoint
from src.Exports      import Exports
from src.Imports      import Imports
import Rest_API.examples as e
import Rest_API.serializers as s


from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse
import logging
    
logger = logging.getLogger('Rest_API.views')

###########################################################################################
class GatherAll(APIView):
    @extend_schema(
        description="This endpoint queries the FAF database and retrieves one of six fully populated tables: faf0, faf1, faf2, faf3, state0, state1, state2, or state3. Subsequently, the server generates a query to join these smaller tables with the main data tables and processes this query. The resulting data is stored in a Pandas DataFrame, converted to a CSV file, and provided to the user as a downloadable file. The file is named according to the selected table. If the user inputs incorrect information, an error message is returned detailing the issue.",
        examples=[
            OpenApiExample(
                'Example',
                value = e.tableModel_example,
                media_type="application/json",
            )
        ],
        request=s.TableSerializer(),
        responses={
            '200': OpenApiResponse(
                description= "CSV download of joined data table",
                    )
        }
    )
    def post(self, request):
        serializer = s.TableSerializer(data=request.data)
        if serializer.is_valid():
            table  = serializer.validated_data['table']
            gt   = GrabTable(table)
            if gt.fail == 1: return Response("ERROR: Wrong Table")
            query = gt.setup()
             
            logger.info(f"Grab Table Query: {query}")
            
            lookup = QueryTool()
            data = lookup.query(query)
            try:
                csv_data = data.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = f'attachment; filename={request.data["table"]}.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)

###########################################################################################
class PointtoPoint(APIView):
    @extend_schema(
        description="This endpoint takes in a specific commodity, or writing “all” gives all the commodities traded between two areas. This endpoint works for both the FAF and state databases and will return the value and quantity per ton of the resource traded between the origin and destination based on year or timeframe if given two years. This endpoint also returns the method of transportation, and if either the origin or destination is foreign, it returns the foreign transit and any other states the commodity moved to before the final destination.",
        examples=[
            OpenApiExample(
                'Single Year Example',
                value=e.PointToPointExample1,
                media_type="application/json",
            ),
            OpenApiExample(
                'Year Range Example',
                value=e.PointToPointExample2,
                media_type="application/json",
            ),
            OpenApiExample(
                'Response Example',
                value=e.PtoPReturnExample,
                media_type="application/json",
            )
        ],
        request=s.PointToPointSerializer(),
        responses={
            '200':s.PtoPReturnSerializer(many=True),
        },
    )

    def post(self, request):
        serializer = s.PointToPointSerializer(data=request.data)
        if serializer.is_valid():
            data = PointToPoint(
                serializer.validated_data['commodity'],
                serializer.validated_data['origin'],
                serializer.validated_data['destination'],
                serializer.validated_data['timeframe']
            )
            query = data.setup()
            if query == False: return Response("ERROR: Check data") 
            logger.info(f"PointToPoint: {query}")
            lookup = QueryTool()
            data = lookup.query(query)
            try:
                csv_data = data.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = 'attachment; filename=PointToPoint.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)

##########################################################################################
class Export_endpoint(APIView):
    @extend_schema(
        description="This endpoint takes in a region or state with a year or year frame and returns all exported commodities from that area. This only applies to domestic-based trade. The endpoint returns the commodity type, the transportation type, the area the commodity was sent to, and the year's ton and value.",
        examples=[
            OpenApiExample(
                'Single Year Example',
                value=e.exportSingleExample1,
                media_type="application/json",
            ), 
            OpenApiExample(
                'Year Window Example',
                value=e.exportMultiExample2,
                media_type="application/json",
            ),
           OpenApiExample(
                'Return Example',
                value=e.exportReturnExample,
                media_type="application/json",
            )

        ],
        request=s.ExportsSerializer(),
        responses={
            '200':s.ExportsReturnSerializer(many=True)
        },
    )

    def post(self, request):
        serializer = s.ExportsSerializer(data=request.data)
        if serializer.is_valid():
            data = Exports(
                serializer.validated_data['origin'],
                serializer.validated_data['timeframe']
            )
            query = data.setup()

            if query == False: return Response("Error: Check Data", 400)
            logger.info(f"Export Endpoint:{query}")
            lookup = QueryTool()
            data = lookup.query(query)
            try:
                csv_data = data.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = f'attachment; filename=exports_{serializer.validated_data["origin"]}.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)

 
##########################################################################################
class Import_endpoint(APIView):
    @extend_schema(
        description="This endpoint takes in a region or state with a year or year frame and returns all imported commodities from that area. This only applies to domestic-based trade. The endpoint returns the commodity type, the transportation type, the area the commodity was sent to, and the year's ton and value.",
        examples=[
            OpenApiExample(
                'Single Year Example',
                value=e.exportSingleExample1,
                media_type="application/json",
            ), 
            OpenApiExample(
                'Year Window Example',
                value=e.exportMultiExample2,
                media_type="application/json",
            ),
           OpenApiExample(
                'Return Example',
                value=e.importReturnExample,
                media_type="application/json",
            )

        ],
        request=s.ImportsSerializer(),
        responses={
            '200':s.ImportsReturnSerializer(many=True)
        }
    )

    def post(self, request):
        serializer = s.ImportsSerializer(data=request.data)
        if serializer.is_valid():
            data = Imports(
                serializer.validated_data['origin'],
                serializer.validated_data['timeframe']
            )
            query = data.setup()

            if query == False: return Response("Error: Check Data", 400)
            logger.info(f"Export Endpoint:{query}")
            lookup = QueryTool()
            data = lookup.query(query)
            try:
                csv_data = data.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = f'attachment; filename=Imports_{serializer.validated_data["origin"]}.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)


##########################################################################################
#fr_import
#fr_export
##########################################################################################
class RawResource(APIView):
    @extend_schema(
        description="This endpoint takes in an origin named and a year/year frame and calculates the sum of each resource imported and exported from the said area. It returns data by giving the area’s name, the resource, whether it was imported or exported, and the summation of said resource based on year. Currently this only works for domestic imports and outports",
        examples=[
            OpenApiExample(
                'Example Year',
                value=e.rawExample1,
                media_type="application/json",
            ), 
            OpenApiExample(
                'Example Year Frame',
                value=e.rawExample2,
                media_type="application/json",
            ),
            OpenApiExample(
                'Return Example',
                value=e.rawExampleReturn,
                media_type="application/json",
            ),
        ],
        request=s.RawResourceSerializer(),
        responses={
            '200':s.RawResourceReturnSerializer(many=True)
        }
    )
    def post(self, request):
        serializer = s.RawResourceSerializer(data=request.data)
        if serializer.is_valid():
            #Send data to class and return data as pandas framework
            gen_query = Imports(
                serializer.validated_data['origin'],
                serializer.validated_data['timeframe']
            )
 
            gen_query2 = Exports(
                serializer.validated_data['origin'],
                serializer.validated_data['timeframe']
            )
            
            #Add ton value based on column and commodity type
            query  = gen_query.setup()
            query2 = gen_query2.setup()
            logger.info(f"SumRaw:{query}\n{query2}")
            if query == False: return  Response("Error: Check Data", 400)
            if query2 == False: return Response("Error: Check Data2", 400)
            lookup = QueryTool()
            self.df1 = lookup.query(query)
            self.df2 = lookup.query(query2)
            commodities = lookup.query("SELECT description FROM c")["description"]
            
            #splitting proccess between 1 and 2, will join both dataframes in end
            output1 = {
                "origin"   : [],
                "commodity": [],
                "option":    [],
            }
            output2 = {
                "origin"   : [],
                "commodity": [],
                "option":    [],
            }
 
            for col  in self.df1:
                if col[:4] == 'tons':
                    output1[col] = []
                
                    for c in commodities:
                        if c not in output1['commodity']:
                            output1['origin'].append(serializer.validated_data['origin'])
                            output1['commodity'].append(c)
                            output1['option'].append("Imports")
                        output1[col].append(self._quickSum(1, c, col))
            for col  in self.df2:
                if col[:4] == 'tons':
                    output2[col] = []
                
                    for c in commodities:
                        if c not in output2['commodity']:
                            output2['origin'].append(serializer.validated_data['origin'])
                            output2['commodity'].append(c)
                            output2['option'].append("Exports")
                        output2[col].append(self._quickSum(0, c, col))
            
            new_df1 = pd.DataFrame(output1)
            new_df2 = pd.DataFrame(output2)
            #joined dataframe
            complete_df = pd.concat([new_df1, new_df2])
            try:
                csv_data = complete_df.to_csv(index=False)
                response = HttpResponse(csv_data, content_type="text/csv")
                response['Content-Disposition'] = f'attachment; filename=SumImportOutports{serializer.validated_data["origin"]}.csv'
                return response
            except:
                return Response("ERROR: Cannot return csv_data")
        return Response(serializer.errors, status=400)



    def _quickSum(self, n, check, sumcol):
        if n: filtered_df = self.df1[self.df1['Commodity'] == check]
        else: filtered_df = self.df2[self.df2['Commodity'] == check]
        return filtered_df[sumcol].sum()
##########################################################################################
class Commodity_total(APIView):
    @extend_schema(
        description="Takes the commodities in each state and adds up their total based on import, export or both and sorts the return based on ton amount. The time frame is based on year or year frame, and the return will give the location of the ranked commodity and if it was imported or exported",
        examples=[
            OpenApiExample(
                'Example Year',
                value=e.commtotalExample1,
                media_type="application/json",
            ), 
            OpenApiExample(
                'Example TimeFrame',
                value=e.commtotalExample2,
                media_type="application/json",
            ),
           OpenApiExample(
                'Return Example',
                value=e.commtotalReturnExample,
                media_type="application/json",
            ),

        ],
        request=s.CommodityTotalSerializer(),
        responses={
            '200':s.CommodityTotalReturnSerializer(many=True)
        }
    )
    def post(self, request):
        return Response("Commodity total is up!")
##########################################################################################
