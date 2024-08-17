import src.queries.Mapping as metrics
class GrabTable:
    def __init__(self,
            table     = "_faf551_faf_0",
            origin    = 1, 
            dest      = 1, 
            commodity = 1, 
            tport     = 1, 
            dist      = 1,
            ton_y     = [],
            val_y     = [],
            curVal_y  = [],
            tmile     = [],
            tonHigh_y = [],
            tonLow_y  = [],
            valHigh_y = [],
            valLow_y  = [],
            limit     = 30,
    ):
        self.query = "SELECT "
        self.table     = table
        self.origin    = 1
        self.dest      = 1
        self.commodity = 1
        self.tport     = 1
        self.dist      = 1
        self.ton_y     = [x for x in metrics.tons.keys()]
        self.val_y     = val_y 
        self.curVal_y  = curVal_y 
        self.tmile     = tmile 
        self.tonHigh_y = tonHigh_y 
        self.tonLow_y  = tonLow_y 
        self.valHigh_y = valHigh_y 
        self.valLow_y  = valLow_y 
        self.limit     = limit 


    def setup(self):
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

    def help(self):
        help_data = {}
        try: metrics.table[self.table.strip()]
        except:help_data['table'] = [x for x in metrics.table.keys()]

        if 'help' in self.ton_y: help_data['tons']             = [x for x in metrics.tons.keys()]
        if 'help' in self.val_y: help_data['value']            = [x for x in metrics.value.keys()]
        if 'help' in self.curVal_y: help_data['current_value'] = [x for x in metrics.current_value.keys()]
        if 'help' in self.tmile: help_data['tmiles']           = [x for x in metrics.tmiles.keys()]
        if 'help' in self.tonHigh_y: help_data['tonHigh']      = [x for x in metrics.tons_high.keys()]
        if 'help' in self.tonLow_y: help_data['tonLow']        = [x for x in metrics.tons_low.keys()]
        if 'help' in self.valHigh_y: help_data['valueHigh']    = [x for x in metrics.value_high.keys()]
        if 'help' in self.valLow_y: help_data['valueLow']      = [x for x in metrics.value_low.keys()]
        if help_data: return help_data
        return 0   

    def _table(self):
        self.query += f"FROM {metrics.table[self.table]} "

    def _columnsfaf(self):
        cols = []
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
            
        if cols: return cols
        return 0

