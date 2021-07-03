import sqlite3
import time
import pandas as pd
con = sqlite3.connect("./database/arrayinfo.db")
cursor = con.cursor()
check_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

def create_new_table(framework_name):
    # 테이블-필드 생성
    try:
        query = "CREATE TABLE "+str(framework_name)+"(id integer primary key autoincrement, function_name text, function_info text);"
        print("created new table. ")
        print("-"* 100)
        print("name : {0}, created_date : {1}".format(framework_name, check_time))
        print("query : ", query)
        cursor.execute(query)
        con.commit()
    except:
        pass

def create_new_record(framework_name, idx, function_name, function_info):
    # 레코드 생성
    try:
        query = "INSERT INTO "+str(framework_name)+" VALUES("+str(idx)+" , "+str(function_name)+" , "+str(function_info)+");"
        print("query : ", query)
        cursor.execute(query)
        con.commit()
    except:
        pass

def read_record(framework_name):
    # 레코드 조회
    try:
        query = "SELECT * FROM "+str(framework_name)+";"
        print("query : ", query)
        print("\t")
        print("data")
        cursor.execute(query)
        con.commit()
        print("-" * 100)
        data = pd.read_sql(query, con=con)
        print(data)
    except:
        pass
    # finally:
    #     con.close()

def update_record():
    pass

def delete_table():
    pass

def delete_record(framework_name, idx, choice_all=None):
    # 레코드 삭제
    if choice_all is not None:
        print("all data deleted...")
        print("-" * 100)
        query = "DELETE FROM "+str(framework_name)+";"
        print("query : ", query)
        cursor.execute(query)
        con.commit()
    else:
        query = "DELETE FROM "+str(framework_name)+" where id="+str(idx)+";"
        print("query : ", query)
        cursor.execute(query)
        con.commit()

def close_db():
    con.close()

create_new_table("mxnet")
create_new_record("mxnet", 1, "'테스트1'", "'테스트11'")
create_new_record("mxnet", 2, "'테스트2'", "'테스트12'")
# delete_record("mxnet", 1, choice_all=None)
read_record("mxnet")
close_db()