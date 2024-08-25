from src.Data_Lookup import QueryTool
import src.queries.faf_map   as fm
import src.queries.state_map as sm

class Export:
    """
    This class generates a query for all of the exports comming out of a particular location.
    origin(string): the location which can be in state or regional
    timeframe(list of int): this attrubute gives the timeframe of data being requested
    """
    def __init__(
            self,
            origin    = "",
            timeframe = [],
    ):
        self.query = "SELECT "

        self.origin    = origin
        self.table     = None
        self.timeframe = timeframe

    def setup(self):
        self.table = self._checkLocations()
        if self.table == False: return False        #incorrect origin destination match
        if not self._checkTimeframe(): return False #incorrect times
        cols = []

        if self.table[:3] == "faf":
            cols.append(fm.faf["dms_orig"][0])
            cols.append(fm.faf["dms_dest"][0])
            cols.append(fm.faf["sctg2"][0])
            cols.append(fm.faf["dms_mode"][0])

        else:
            cols.append(sm.state["dms_orig"][0])
            cols.append(sm.state["dms_dest"][0])
            cols.append(sm.state["sctg2"][0])
            cols.append(sm.state["dms_mode"][0])

        if self.table[:3] == "faf":
            for year in self.timeframe:
                try: cols.append(fm.tons[str(year)])
                except: continue
            for year in self.timeframe:
                try: cols.append(fm.value[str(year)])
                except: continue
        else:
             for year in self.timeframe:
                try: cols.append(sm.tons[str(year)])
                except: continue
             for year in self.timeframe:
                try: cols.append(sm.value[str(year)])
                except: continue

        self.query += ", ".join(cols) + " "

        self._table()

        if self.table[:3] == "faf":
            self.query += fm.faf["dms_orig"][1] + " "
            self.query += fm.faf["dms_dest"][1] + " "
            self.query += fm.faf["sctg2"][1] + " "
            self.query += fm.faf["dms_mode"][1] + " "

        else:
            self.query += sm.state["dms_orig"][1] + " "
            self.query += sm.state["dms_dest"][1] + " "
            self.query += sm.state["sctg2"][1] + " "
            self.query += sm.state["dms_mode"][1] + " "


        #Checks for where statements
        where = "WHERE"

        if self.table == "faf1":
            self.query += f"{where} {fm.abv['faf1']}.description = '{self.origin}' "

        if self.table == "state1":
            self.query += f"{where} {sm.abv['state1']}.description = '{self.origin}' "

        self.query += ";"
        return self.query



    def _table(self):
        """
        Just impends the FROM command with the actual table name to the query
        """
        t = fm.table[self.table]
        a = fm.abv[self.table]
        self.query += f"FROM {t} {a}"


    def _checkLocations(self):
        """Checks the locations and sets table based on origin and destination"""
        tool = QueryTool()
        ostate = tool.query("SELECT description FROM o_state;")
        ofaf   = tool.query("SELECT description FROM o_faf;")
        fo     = tool.query("SELECT description FROM fo;")
        #retrive the table
        if any(o == self.origin for o in ostate['description']):
            return 'state1'

        if any(o == self.origin for o in ofaf['description']):
            return 'faf1'

        if any(o == self.origin for o in fo['description']):
            return 'both'

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

