terms = [('Fr_orig','Foreign region of shipment origin'), ('Fr_dest','Foreign region of shipment destination'), ('Fr_inmode','mode used b/w foreign and US entry region'), ('Fr_outmode','mode b/w US exit region and foreign region'), ('Dms_orig','domestic origin'), ('Dms_dest','domestic destination'), ('Dms_mode','mode b/w domestic origin and destination'), ('Sctg2','standard classification of transported goods'),('Value','total value of commodities shipped'), ('Tons','total weight of commodities shipped'), ('Current_value','total value of commodities shipped')]

table_dict = {
    '_faf551_faf_0'        : 'Regional 0',
    '_faf551_faf_1'        : 'Regional 1',  #domestic origins domestic destinations
    '_faf551_faf_2'        : 'Regional 2',  #foreign origins  domestic destinations
    '_faf551_faf_3'        : 'Regional 3',  #domestic origins foreign destinations
    '_faf551_state_0'      : 'State 0',
    '_faf551_state_1'      : 'State 1',     #domestic origins domestic destinations
    '_faf551_state_2'      : 'State 2',     #foreign origins  domestic destinations
    '_faf551_state_3'      : 'State 3',     #domestic origins foreign destinations
    'c'                    : 'Commodity Type',
    'd_faf'                : 'FAF Domestic Region',
    'd_faf_alphabetical'   : 'FAF Domestic Region Alphabetical',
    'd_state'              : 'Destination State',
    'db'                   : 'Distance Band',
    'fd'                   : 'Foreign Destination',
    'fdm'                  : 'Foreign Destination Mode',
    'fo'                   : 'Foreign Origin',
    'fom'                  : 'Foreign Origin Mode',
    'geo_level'            : 'Geo Zone',
    'm'                    : 'Mode',
    'measure'              : 'Measure',
    'o_faf'                : 'Inside State Origin',
    'o_faf_alphabetical'   : 'State Origin Alphabetical',
    'o_state'              : 'Origin State',
    'tt'                   : 'Type',
    'year_faf'             : 'Year',
    'year_faf_alphabetical': 'Year Alphabetical',
    'year_state'           : 'Year State'
}
