from database.connector import Connector
import argparse
import time
import pandas as pd

def get_args():
    parser = argparse.ArgumentParser(description='CRUD')
    parser.add_argument('--action', type=str, 
        help='create, read, update, delete')
    parser.add_argument('--lib_name', type=str, 
                    help='ML library name')
    parser.add_argument('--db_tool', type=str, 
    default="sqlite", help='database tool, default : sqlite')
    parser.add_argument('--idx', type=int, 
        help='index number')
    parser.add_argument('--f_name', type=str, 
                help='function name')
    parser.add_argument('--f_info', type=str, 
            help='function infomation')
    parser.add_argument('--del_all', type=str, default=None,
        help='if press y, data is deleted.')
    args = parser.parse_args()
    return args

args = get_args()

class DBManager(Connector):
    def __init__(self, db_tool):
        super().__init__(db_tool)

        self.check_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def create_new_table(self, library_name):
        self.connect()
        # 테이블-필드 생성
        query = "CREATE TABLE "+str(library_name)+ \
            "(id integer primary key autoincrement, function_name text, function_info text);"
        print("created new table. ")
        print("-"* 100)
        print("name : {0}, created_date : {1}".format(library_name, self.check_time))
        print("query : ", query)
        self.cursor.execute(query)
        self.con.commit()

    def create_new_record(self, library_name, idx, function_name, function_info):
        # 레코드 생성
        self.connect()
        query = "INSERT INTO "+str(library_name)\
            +" VALUES("+str(idx)+" , "+str(function_name)\
            +" , "+str(function_info)+");"
        print("query : ", query)
        self.cursor.execute(query)
        self.con.commit()

    def read_record(self, library_name):
        # 레코드 조회
        self.connect()
        query = "SELECT * FROM "+str(library_name)+";"
        print("query : ", query)
        print("\t")
        print("data")
        self.cursor.execute(query)
        self.con.commit()
        print("-" * 100)
        data = pd.read_sql(query, con=self.con)
        print(data)

    def update_record(self):
        pass

    def delete_table(self):
        pass

    def delete_record(self, library_name, idx, choice_all=None):
        # 레코드 삭제
        self.connect()
        if choice_all is not None:
            print("all data deleted...")
            print("-" * 100)
            query = "DELETE FROM "+str(library_name)+";"
            print("query : ", query)
            self.cursor.execute(query)
            self.con.commit()
        else:
            query = "DELETE FROM "+str(library_name)+" where id="+str(idx)+";"
            print("query : ", query)
            self.cursor.execute(query)
            self.con.commit()

    def close_db(self):
        self.connect()
        self.con.close()

manager = DBManager(args.db_tool)

if args.action == "ct":
    manager.create_new_table()
if args.action == "cr":
    manager.create_new_record(args.lib_name, args.idx, args.f_name, args.f_info)
if args.action == "rr":
    manager.read_record(args.lib_name)
if args.action == "dr":
    manager.delete_record(args.lib_name, args.idx, args.del_all)
