from src.Data_Lookup import QueryTool
import src.queries.faf_mapping   as metrics
import src.queries.state_mapping as sm
class PointToPoint:
    def __init__(self,
            commodity = "all",
            origin    = "",
            dest      = "",
            timeframe = [],
            limit     = 30,
    ):
        self.query = "SELECT "

        self.commodity = commodity
        self.dest      = dest
        self.table     = None
        self.tport     = 1
        self.ton_y     = timeframe
        self.val_y     = timeframe 
        self.limit     = limit 
        
        table          = ""

    def setup(self):
        return self._checkCommodity()
        

        cols = []
        if self.origin    == True: cols.append(metrics.faf0["dms_orig"][0])
        if self.dest      == True: cols.append(metrics.faf0["dms_dest"][0])
        if self.commodity == True: cols.append(metrics.faf0["sctg2"][0])
        if self.tport     == True: cols.append(metrics.faf0["dms_mode"][0])
        if self.dist      == True: cols.append(metrics.faf0["dist_band"][0])
    
        for year in self.ton_y:
            try: cols.append(metrics.tons[year.strip()])
            except: continue

        for year in self.val_y:
            try: cols.append(metrics.value[year.strip()])
            except: continue

        for year in self.curVal_y:
            try: cols.append(metrics.current_value[year.strip()])
            except: continue

        for year in self.tmile:
            try: cols.append(metrics.tmiles[year.strip()])
            except: continue

        for year in self.tonHigh_y:
            try: cols.append(metrics.tons_high[year.strip()])
            except: continue

        for year in self.tonLow_y:
            try: cols.append(metrics.tons_low[year.strip()])
            except: continue

        for year in self.valHigh_y:
            try: cols.append(metrics.value_high[year.strip()])
            except: continue

        for year in self.valLow_y:
            try: cols.append(metrics.value_low[year.strip()])
            except: continue
          
        self.query += ", ".join(cols) + " "

        self._table()

        if self.origin    == True: self.query += metrics.faf0["dms_orig"][1] + " "
        if self.dest      == True: self.query += metrics.faf0["dms_dest"][1] + " "
        if self.commodity == True: self.query += metrics.faf0["sctg2"][1] + " "
        if self.tport     == True: self.query += metrics.faf0["dms_mode"][1] + " "
        if self.dist      == True: self.query += metrics.faf0["dist_band"][1] + " "
        if self.limit > 0: self.query += f"LIMIT {self.limit}"
        self.query += ";"

        return self.query

    def _table(self):
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
        fdstate = tool.query("SELECT description FROM fd;")
        fdfaf   = tool.query("SELECT description FROM fd;")
        fostate = tool.query("SELECT description FROM fo;")
        fofaf   = tool.query("SELECT description FROM fo;")
