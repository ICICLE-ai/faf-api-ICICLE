import src.queries.faf_mapping as metrics
import src.queries.state_mapping as sm

class GrabTable:
    def __init__(self,
            table     = "faf0",
            limit     = 0,       #debug purposes 0 means all, x>0 sets limit
    ):
        self.query    = "SELECT "
        self.table    = table
        self.limit    = limit
        
        #checks for wrong table input
        self.fail     = 0
        try: metrics.table[table]
        except: self.fail = 1


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
            [cols.append(year) for year in metrics.tons.values()]
            [cols.append(year) for year in metrics.value.values()]
            [cols.append(year) for year in metrics.current_value.values()]
            [cols.append(year) for year in metrics.tmiles.values()]
            [cols.append(year) for year in metrics.tons_high.values()]
            [cols.append(year) for year in metrics.tons_low.values()]
            [cols.append(year) for year in metrics.value_high.values()]
            [cols.append(year) for year in metrics.value_low.values()]
          
        else:
            [cols.append(year) for year in sm.tons.values()]
            [cols.append(year) for year in sm.value.values()]
            [cols.append(year) for year in sm.current_value.values()]
            [cols.append(year) for year in sm.tmiles.values()]
            [cols.append(year) for year in sm.tons_high.values()]
            [cols.append(year) for year in sm.tons_low.values()]
            [cols.append(year) for year in sm.value_high.values()]
            [cols.append(year) for year in sm.value_low.values()]
        

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

        return self.query

    def _table(self):
        self.query += f"FROM {metrics.table[self.table]} "
