from src.Data_Lookup import QueryTool
import src.queries.faf_mapping   as metrics
import src.queries.state_mapping as sm
class PointToPoint:
    """
    This generates a query that looks at one directional trade between two locations; the origin to the destination. 

    commodity(str): type of commodity. If 'all' then all commodities are returned
    origin(str): location 1 
    dest(str):   location 2
    timeframe(list of int): this attrubute gives the timeframe of data being requested
    """
    def __init__(self,
            commodity = "all",
            origin    = "",
            dest      = "",
            timeframe = [],
    ):
        self.query = "SELECT "

        self.commodity = commodity
        self.dest      = dest
        self.origin    = origin
        self.table     = None
        self.timeframe = timeframe


    def setup(self):
        if not self._checkCommodity(): return False #incorrect commodity type
        self.table = self._checkLocations()
        if self.table == False: return False        #incorrect origin destination match
        if not self._checkTimeframe(): return False #incorrect times 
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

        else:
            if self.table == "state2" :cols.append(sm.state2["fr_orig"][0])
            cols.append(sm.state0["dms_orig"][0])
            cols.append(sm.state0["dms_dest"][0])
            if self.table == "state3" :cols.append(sm.state3["fr_dest"][0])
            cols.append(sm.state0["sctg2"][0])
            if self.table == "state2" :cols.append(sm.state2["fr_inmode"][0])
            cols.append(sm.state0["dms_mode"][0])
            if self.table == "state3" :cols.append(sm.state3["fr_outmode"][0])   
 
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
            if self.table == "faf2" :self.query += metrics.faf2["fr_orig"][1] + " "
            self.query += metrics.faf0["dms_orig"][1] + " "
            self.query += metrics.faf0["dms_dest"][1] + " "
            if self.table == "faf3" :self.query += metrics.faf3["fr_dest"][1] + " "
            self.query += metrics.faf0["sctg2"][1] + " "
            if self.table == "faf2" :self.query += metrics.faf2["fr_inmode"][1] + " "
            self.query += metrics.faf0["dms_mode"][1] + " "
            if self.table == "faf3" :self.query += metrics.faf3["fr_outmode"][1] + " "

        else:
            if self.table == "state2" :self.query += sm.state2["fr_orig"][1] + " "
            self.query += sm.state0["dms_orig"][1] + " "
            self.query += sm.state0["dms_dest"][1] + " "
            if self.table == "state3" :self.query += sm.state3["fr_dest"][1] + " "
            self.query += sm.state0["sctg2"][1] + " "
            if self.table == "state2" :self.query += sm.state2["fr_inmode"][1] + " "
            self.query += sm.state0["dms_mode"][1] + " "
            if self.table == "state3" :self.query += sm.state3["fr_outmode"][1] + " "


        #Checks for where statements
        where = "WHERE"
        if self.commodity != 'all': 
            self.query += f"{where} c.description = '{self.commodity}' "
            where = "AND"
        
        if self.table == "faf0" or self.table == "faf1":
            self.query += f"{where} of0.description = '{self.origin}' "
            where = "AND"
            self.query += f"{where} df.description = '{self.dest}' "        

        if self.table == "faf2":
            self.query += f"{where} fo.description = '{self.origin}' "
            where = "AND"
            self.query += f"{where} df.description = '{self.dest}' "        

        if self.table == "faf3":
            self.query += f"{where} of0.description = '{self.origin}' "
            where = "AND"
            self.query += f"{where} fd.description = '{self.dest}' "        

        if self.table == "state0" or self.table == "state1":
            self.query += f"{where} os.description = '{self.origin}' "
            where = "AND"
            self.query += f"{where} ds.description = '{self.dest}' "        

        if self.table == "state2":
            self.query += f"{where} fo.description = '{self.origin}' "
            where = "AND"
            self.query += f"{where} ds.description = '{self.dest}' "        

        if self.table == "state3":
            self.query += f"{where} os.description = '{self.origin}' "
            where = "AND"
            self.query += f"{where} fd.description = '{self.dest}' "        


        self.query += ";"
        return self.query



    def _table(self):
        """
        Just impends the FROM command with the actual table name to the query
        """
        self.query += f"FROM {metrics.table[self.table]} "

    def _checkCommodity(self):
        """Checks if commodity is in table. If not, returns commodity list"""
        if self.commodity.lower() == 'all': return True
        tool = QueryTool()
        c    = tool.query("SELECT description FROM c;")
        
        for comm in c['description']:
            if comm == self.commodity: return True
        return False
       
    def _checkLocations(self):
        """Checks the locations and sets table based on origin and destination""" 
        tool = QueryTool()
        dstate = tool.query("SELECT description FROM d_state;")
        dfaf   = tool.query("SELECT description FROM d_faf;")
        ostate = tool.query("SELECT description FROM o_state;")
        ofaf   = tool.query("SELECT description FROM o_faf;")        
        fd = tool.query("SELECT description FROM fd;")
        fo = tool.query("SELECT description FROM fo;")

        for state in ostate['description']:
            if state == self.origin:
                for snd in dstate['description']:
                    if snd == self.dest: return "state1"
                for snd in fd['description']:
                    if snd == self.dest: return "state3"

        for faf in ofaf['description']:
            if faf == self.origin:
                for snd in dfaf['description']:
                    if snd == self.dest: return "faf1"
                for snd in fd['description']:
                    if snd == self.dest: return "faf3"

        for area in fo['description']:
            if area == self.origin:
                for snd in dstate['description']:
                    if snd == self.dest: return "state2"
                for snd in dfaf['description']:
                    if snd == self.dest: return "faf2"
        return False

    def _checkTimeframe(self):        
        """
        Chcks to make sure the numbes of years in timeframe are not 0 or more than 2. Then if there are two years, this method populates the years inbetween
        """
        tf = self.timeframe
        if   len(tf) > 2:  return False
        elif len(tf) == 0: return False
        elif len(tf) == 2: self.timeframe = [x for x in range(tf[0], tf[1]+1)]
        return True
