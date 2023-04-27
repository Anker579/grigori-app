from db_connector import DBCommunicator
from api_connector import WeatherApi
from emailer import email_bot


my_db_comm = DBCommunicator()
my_email_bot = email_bot()


my_weather_api = WeatherApi()
response = my_weather_api.get_response_OW()
time = my_weather_api.get_time()

if my_weather_api.check_response(response=response) == True:
    data = my_weather_api.create_dict_OW(response=response, time=time)
elif not my_weather_api.check_response(response):
    response = my_weather_api.get_response_WU()
    data = my_weather_api.create_dict_WU(response=response, time=time)
else:
    my_email_bot.email_me()

database = my_db_comm.db_connector()
cursor = my_db_comm.create_cursor(database)
sql = my_db_comm.create_sql_string()
data_tuple = my_db_comm.create_data_tuple(data)

cursor.execute(sql, data_tuple)
database.commit()

print("success")