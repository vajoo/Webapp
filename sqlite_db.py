import sqlite3
import pandas as pd

class live_ticker_db:
    def __init__(self, db_name):
        self.conn = sqlite3.connect('C:\\Users\\lauri\\Documents\\GitHub\\Projekt_Tradingbot\\' + db_name + '.db')
        self.c = self.conn.cursor()

    def get_table_entry(self, table, symbol):
        # return python dictionary or json
        with self.conn:
            self.c.execute("SELECT * FROM {} WHERE Symbol = '{}'".format(table, symbol))
            #self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            #print(self.c.fetchall())
        tuple = self.c.fetchall()[0]
        dic = {}
        dic["TI"] = table
        dic["Symbol"] = tuple[0]
        dic["Parameter"] = tuple[1]
        dic["Performance"] = tuple[2]
        dic["Trades"] = tuple[3]
        dic["Signal"] = tuple[4]
        return dic
            
    def check_if_table_exist(self, technical_indicator):
        with self.conn:
            self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(technical_indicator))
            if self.c.fetchone() != None:
                return True
            else:
                return False

    def get_all_tables(self):
        with self.conn:
            self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        result = self.c.fetchall()
        new_list = []
        for i in result:
            new_list.append(i[0])
        return new_list