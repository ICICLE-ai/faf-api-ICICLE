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
    def connectSQL(self):
        self.engine = create_engine(self.connection)
        self.conn   = self.engine.connect()

    def tables(self):
        return [x for x in m.table_dict.values()]

    def show_db(self):      
        self.engine = create_engine(self.connection)
        with self.engine.connect() as con:
            sql_query = "SHOW TABLES;"

            #seralize and map tables
            r = con.execute(text(sql_query))
            table_mapped = []
            for tb in r:
                try: table_mapped.append(m.table_dict[tb[0]])
                except: table_mapped.append(tb[0])

            return table_mapped

    def query(self, string):
        self.engine = create_engine(self.connection)
        with self.engine.connect() as con:
            
            table = []
            r = con.execute(text(string))
            
            #seralize to get all data from each entry
            index = 0
            for unit in r:
                for spot in range(len(unit)):
                    try: table[index].append(unit[spot])
                    except: table.append([unit[spot]])
                index +=1

            return table
        
