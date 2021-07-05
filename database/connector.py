import sqlite3

class Connector:
    def __init__(self, db_tool):
        self.db_tool = db_tool
        self.con = None
        self.cursor = None
    
    def connect(self):
        if self.db_tool == "sqlite":
            self.con = sqlite3.connect("./database/arrayinfo.db")
            self.cursor = self.con.cursor()