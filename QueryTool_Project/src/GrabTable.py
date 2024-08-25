import src.queries.faf_mapping as metrics
import src.queries.state_mapping as sm

class GrabTable:
    """
    This class generates a query for MySQL by using the lookup tables imported above to populate a specific table with information.

    *table(string): this attribute is the name of the table that will be used in the mysql db

    *timeframe(list of int): this attrubute gives the timeframe of data being requested

    *limit(int): This limits the data being sent for debugging purposes, but isn't implemented automatically. 0 means all the data, any number above zero is the number of rows being returned.
    """ 
    def __init__(self,
            table     = "faf0",
            timeframe = [],
            limit     = 0,       #debug purposes 0 means all, x>0 sets limit
    ):
        self.query     = "SELECT "
        self.table     = table
        self.timeframe = timeframe
        self.limit     = limit
        
        #checks for wrong table input
        self.fail     = 0
        try: metrics.table[table]
        except: self.fail = 1
        
        if not self._checkTimeframe(): return False
    
    def setup(self):
        cols = []

        if self.table[:3] == "faf":
            if self.table == "faf2" :cols.append(metrics.faf2["fr_orig"][0]) 
            cols.append(metrics.faf0["dms_orig"][0])
            cols.append(metrics.faf0["dms_dest"][0])
            if self.table == "faf3" :cols.append(metrics.faf3["fr_dest"][0]) 
            cols.append(metrics.faf0["sctg2"][0])
            if self.table == "faf2" :cols.append(metrics.faf2["fr_inmode"][0]) 
            cols.append(metrics.faf0["dms_mode"][0])
            if self.table == "faf3" :cols.append(metrics.faf3["fr_outmode"][0]) 
            cols.append(metrics.faf0["dist_band"][0])
    
        else:
            if self.table == "state2" :cols.append(sm.state2["fr_orig"][0]) 
            cols.append(sm.state0["dms_orig"][0])
            cols.append(sm.state0["dms_dest"][0])
            if self.table == "state3" :cols.append(sm.state3["fr_dest"][0]) 
            cols.append(sm.state0["sctg2"][0])
            if self.table == "state2" :cols.append(sm.state2["fr_inmode"][0]) 
            cols.append(sm.state0["dms_mode"][0])
            if self.table == "state3" :cols.append(sm.state3["fr_outmode"][0]) 
            
        #building the query to select all of the year based data in Mapping.py
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

        #join the tables from the mapping files
        if self.table[:3] == "faf":
            if self.table == "faf2" :self.query += metrics.faf2["fr_orig"][1] + " "
            self.query += metrics.faf0["dms_orig"][1] + " "
            self.query += metrics.faf0["dms_dest"][1] + " "
            if self.table == "faf3" :self.query += metrics.faf3["fr_dest"][1] + " "
            self.query += metrics.faf0["sctg2"][1] + " "
            if self.table == "faf2" :self.query += metrics.faf2["fr_inmode"][1] + " "
            self.query += metrics.faf0["dms_mode"][1] + " "
            if self.table == "faf3" :self.query += metrics.faf3["fr_outmode"][1] + " "
            self.query += metrics.faf0["dist_band"][1] + " "
            if self.limit > 0: self.query += f"LIMIT {self.limit}"
            self.query += ";"

        else:
            if self.table == "state2" :self.query += sm.state2["fr_orig"][1] + " "
            self.query += sm.state0["dms_orig"][1] + " "
            self.query += sm.state0["dms_dest"][1] + " "
            if self.table == "state3" :self.query += sm.state3["fr_dest"][1] + " "
            self.query += sm.state0["sctg2"][1] + " "
            if self.table == "state2" :self.query += sm.state2["fr_inmode"][1] + " "
            self.query += sm.state0["dms_mode"][1] + " "
            if self.table == "state3" :self.query += sm.state3["fr_outmode"][1] + " "
            if self.limit > 0: self.query += f"LIMIT {self.limit}"
            self.query += ";"

        print("\n\n",self.query,"\n\n")
        return self.query

    def _table(self):
        """
        Just impends the FROM command with the actual table name to the query
        """
        self.query += f"FROM {metrics.table[self.table]} "

    def _checkTimeframe(self):
        """
        Chcks to make sure the numbes of years in timeframe are not 0 or more than 2. Then if there are two years, this method populates the years inbetween
        """
        tf = self.timeframe
        if   len(tf) > 2:  return False
        elif len(tf) == 0: return False
        elif len(tf) == 2: self.timeframe = [x for x in range(tf[0], tf[1]+1)]
        return True
