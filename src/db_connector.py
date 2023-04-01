import MySQLdb
import datetime as dt
from dotenv import load_dotenv
import os
# from dotenv import dotenv_values
# config = dotenv_values(".env")

class DBCommunicator():

    def __init__(self) -> None:
        self.HOST = os.environ.get("HOST")
        self.DATABASE = os.environ.get("DATABASE")
        self.USER = os.environ.get("USER")
        self.PASSWORD = os.environ.get("PASSWORD")

    def db_connector(self):
        db = MySQLdb.connect(host=self.HOST,
            database=self.DATABASE,
            user=self.USER,
            password=self.PASSWORD)
        return db

    def create_cursor(self, db):
        curs = db.cursor()
        return curs
    
    def create_sql_string(self):
        sql = ("INSERT INTO pitsford_weather_scrape"
              "(`time`, temp_c, feelslike_c, wx_desc, lat, `long`)"
              "VALUES (%s, %s, %s, %s, %s, %s)")
        
        return sql
    
    def create_data_tuple(self, data_dict):
        '''example data: data = (time, 10, 8, "cold", 51, 8)'''
        time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        temp_c = data_dict["temp_c"]
        feelslike_c = data_dict["feelslike_c"]
        wx_desc = data_dict["wx_desc"]
        lat = data_dict["lat"]
        long = data_dict["long"]
        data = (time, temp_c, feelslike_c, wx_desc, lat, long)
        return data


if __name__ == "__main__":
    my_db_comm = DBCommunicator()
    db = my_db_comm.db_connector()
    curs = my_db_comm.create_cursor(db=db)
    sql = my_db_comm.create_sql_string()
    # data = my_db_comm.create_data_tuple(data_dict=)
    data = ("2023-04-01 10:09:34", 10, 8, "cold", 51, -0.75)
    curs.execute(sql, data)
    db.commit()