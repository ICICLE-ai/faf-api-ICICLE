from sqlalchemy import create_engine, MetaData, Table, text
import src.DB_Mapping as m
import json

class QueryTool:
    def __init__(self, db='faf', usr='fafuser', psswrd='FQ^2t73Ava', host='localhost'):
        self.db     = db
        self.usr    = usr 
        self.psswrd = psswrd
        self.host   = host

        self.engine = None 
        self.conn   = None

        self.connection  = f"mysql+pymysql://{self.usr}:{self.psswrd}@localhost:3306/{self.db}"

    def show_tables(self):      
        self.engine = create_engine(self.connection)
        with self.engine.connect() as con:
            sql_query = "SHOW TABLES;"

            #seralize and map tables
            r = con.execute(text(sql_query))
            return [x[0] for x in r]

    def query(self, string):
        self.engine = create_engine(self.connection)
        with self.engine.connect() as con:
            try:    return self._seralize(con.execute(text(string)))
            except: return ["Incorrect Query"] 

    def colname(self, table):
        self.engine = create_engine(self.connection)
        with self.engine.connect() as con:
             
            if(table):
                sql      = f"DESCRIBE {table}"

                try: sql = con.execute(text(sql))
                except: return ["Incorrect Table-Name"]

                rawDesc = self._seralize( sql )
                desc = []
                for line in rawDesc: desc.append(line[0])
                return desc

    def _seralize(self, data):
        index = 0
        table = []
        for unit in data:
            for spot in range(len(unit)):
                try: table[index].append(unit[spot])
                except: table.append([unit[spot]])
            index +=1
        return table
"""

    def colname(self, table):
        self.engine = create_engine(self.connection)
        with self.engine.connect() as con:
            #tab = [key for key, value in m.table_dict.items() if value == table]
            tab = table
             
            if(tab):
                sql     = f"DESCRIBE {tab}"
                r       = con.execute(text(sql))
                rawDesc = self._seralize( r )

                desc = []
                for line in rawDesc: desc.append(line[0])
                return desc
            else: 
                return "NaN"

    def list_commands(self):
        cmd = {
            'help'      : 'list commands',
            'query'     : 'send a query to the database',
            'column'    : 'get the fields from a table',
            'commodity' : 'shows specific commodity from other tables',
        }
        return cmd

    def allResources(self):
        self.engine = create_engine(self.connection)
        with self.engine.connect() as con:
            r = con.execute("SELECT * FROM c")
            return self._seralize(r)

    def _mapped_tables(self, table):
        return [key for key, value in m.table_dict.items() if value == table][0]

"""
