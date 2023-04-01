from db_connector import DBCommunicator
from api_connector import WeatherApi


my_api_con = WeatherApi()
my_db_comm = DBCommunicator()


my_weather_api = WeatherApi()
response = my_weather_api.get_response()
time = my_weather_api.get_time()
if my_weather_api.check_response(response=response) == True:
    data = my_weather_api.create_dict(response=response, time=time)

database = my_db_comm.db_connector()
cursor = my_db_comm.create_cursor(database)
sql = my_db_comm.create_sql_string()
data_tuple = my_db_comm.create_data_tuple(data)

cursor.execute(sql, data_tuple)
database.commit()

print("success")