from src.Data_Lookup import QueryTool
import src.queries.faf_mapping as metrics
import src.queries.state_mapping as sm
import pandas as pd
class CommodityTotal:
    """
    Generates a MySQL query that gets all of the trading in a speficic time frame based on either state or region. 
    timeframe(list of int): this attrubute gives the timeframe of data being requested
    option(string): either state or region - chooses which tables to build for
    limit(int): for debugging purposes only, limits number of rows. 0 means all.
    """
    def __init__(self,
            timeframe = [], 
            option    = "",
            limit     = 0,
    ):
        self.query = "SELECT "
        
        self.timeframe = timeframe
        self.option    = option
        self.table     = None
        
        self.limit = limit    

    def setup(self):
        err = self._checkLocations()
        if err == False: return self._error("table")

        if not self._checkTimeframe(): return self._error("time")

        

        cols = []
        if self.table[:3] == "faf":
            cols.append(metrics.faf0["dms_orig"][0])
            cols.append(metrics.faf0["dms_dest"][0])
            cols.append(metrics.faf0["sctg2"][0])
        else:
            cols.append(sm.state0["dms_orig"][0])
            cols.append(sm.state0["dms_dest"][0])
            cols.append(sm.state0["sctg2"][0])

        if self.table[:3] == "faf":
            for year in self.timeframe:
                try: cols.append(metrics.tons[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(metrics.value[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(metrics.current_value[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(metrics.tons_high[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(metrics.tons_low[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(metrics.value_high[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(metrics.value_low[str(year)])
                except: continue

        else:
            for year in self.timeframe:
                try: cols.append(sm.tons[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(sm.value[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(sm.current_value[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(sm.tons_high[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(sm.tons_low[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(sm.value_high[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(sm.value_low[str(year)])
                except: continue
        self.query += ", ".join(cols) + " "

        self._table()

        if self.table[:3] == "faf":
            self.query += metrics.faf0["dms_orig"][1] + " "
            self.query += metrics.faf0["dms_dest"][1] + " "
            self.query += metrics.faf0["sctg2"][1] + " "

        else:
            self.query += sm.state0["dms_orig"][1] + " "
            self.query += sm.state0["dms_dest"][1] + " "
            self.query += sm.state0["sctg2"][1] + " "

        if self.limit > 0: self.query += f"LIMIT {self.limit}"
        self.query += ";"

        return self.query


    def _table(self):
        """
        Just impends the FROM command with the actual table name to the query
        """
        self.query += f"FROM {metrics.table[self.table]} "

    def _checkLocations(self):
        """Checks option and sets table to faf0 or state0"""
        if    self.option.lower() == "state": self.table = "state0"
        elif  self.option.lower() == "region": self.table = "faf0"
        else: return False

    def _error(self, code):
        """
        error class that takes in a code and returns a dataframe with the error given
        code(str): error code that is used to create an error specifying the issue
        returns(pandas dataframe): error message
        """
        error = {}
        if   code == "table": 
            error["error"] = ["Error: check option: state or region"]
        elif code == "time": 
            error["error"] = ["Error: check timeframe: ex [2017] or [[2013],[2019]]"]
        else: 
            error["error"] = ["Error: Unknown Error"]      
        return pd.DataFrame(error)

    def _checkTimeframe(self):
        """
        Chcks to make sure the numbes of years in timeframe are not 0 or more than 2. Then if there are two years, this method populates the years inbetween
        """
        tf = self.timeframe
        if   len(tf) > 2:  return False
        elif len(tf) == 0: return False
        elif len(tf) == 2: self.timeframe = [x for x in range(tf[0], tf[1]+1)]
        return True
