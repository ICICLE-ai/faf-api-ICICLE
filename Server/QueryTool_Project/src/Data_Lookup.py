from sqlalchemy import create_engine, MetaData, Table
import src.DB_Mapping as m

class QueryTool:
    def __init__(self, db='faf', usr='fafuser', psswrd='FQ^2t73Ava', host='localhost'):
        self.db     = db
        self.usr    = usr 
        self.psswrd = psswrd
        self.host   = host

        self.engine = None 
        self.conn   = None

    def connectSQL(self):
        connection  = f"mysql+pymysql://{self.usr}:{self.psswrd}@localhost:3306/{self.db}"
        self.engine = create_engine(connection)
        self.conn   = self.engine.connect()

    def tables(self):
        return [x for x in m.table_dict.values()]

    
