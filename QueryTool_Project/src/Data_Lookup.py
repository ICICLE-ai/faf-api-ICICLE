from sqlalchemy import create_engine, MetaData, Table, text
import json
import pandas as pd
import logging
import os
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger('src.Data_Lookup')
class QueryTool:
    """Class takes in the information to log into MySQL
            db    (string) = database name
            usr   (string) = username
            psswrd(string) = password
            host  (string) = hostname
        Returns pandas dataframe
    """
    # def __init__(self, db='faf', usr='root', psswrd='uibi2868', host='localhost'):
    #     self.db     = db
    #     self.usr    = usr
    #     self.psswrd = psswrd
    #     self.host   = host
    def __init__(self, db=None, usr=None, psswrd=None, host=None):
        self.db = db or os.getenv('DB_NAME', 'faf')
        self.usr = usr or os.getenv('DB_USER', 'root')
        self.psswrd = psswrd or os.getenv('DB_PASSWORD', 'uibi2868')
        self.host = host or os.getenv('DB_HOST', 'localhost')

        self.engine = None 
        self.conn   = None

        # self.connection  = f"mysql+pymysql://{self.usr}:{self.psswrd}@localhost:3306/{self.db}"
        self.connection = f"mysql+pymysql://{self.usr}:{self.psswrd}@{self.host}:3306/{self.db}"

        try:
            self.engine = create_engine(self.connection)
            self.conn = self.engine.connect()
            print("✅ Successfully connected to the database.")
        except SQLAlchemyError as e:
            print("❌ Failed to connect to the database.")
            print(f"Error: {e}")


    def query(self, string):
        """
        Takes in a query string and returns a dataframe of information
            - if error in query, returns "Incorrect Query Information" in pandas df
        """
        self.engine = create_engine(self.connection)
        with self.engine.connect() as con:
            try:
                df = pd.read_sql(text(string), con)
                return df
            except:
                logger.info(f"ERROR WITH QUERY: {string}")
                error = {"ERROR": f"Something wrong with Query:{string}"}
                return pd.DataFrame.from_dict(error)
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
