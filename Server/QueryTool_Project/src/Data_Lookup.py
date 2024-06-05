from sqlalchemy import create_engine, MetaData, Table, text
import src.DB_Mapping as m
import json
import pandas as pd

class QueryTool:
    def __init__(self, db='faf', usr='fafuser', psswrd='FQ^2t73Ava', host='localhost'):
        self.db     = db
        self.usr    = usr 
        self.psswrd = psswrd
        self.host   = host

        self.engine = None 
        self.conn   = None

        self.connection  = f"mysql+pymysql://{self.usr}:{self.psswrd}@localhost:3306/{self.db}"


    def query(self, string):
        self.engine = create_engine(self.connection)
        with self.engine.connect() as con:
            df = pd.read_sql(text(string), con)
            return df
"""
    def query(self, string):
        self.engine = create_engine(self.connection)
        with self.engine.connect() as con:
            try: return self._seralize(con.execute(text(string)))
            except: return ["Incorrect Query"] 


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
