import requests
import datetime as dt
import json
from dotenv import load_dotenv
import os
# from dotenv import dotenv_values
# config = dotenv_values(".env")

load_dotenv()

class WeatherApi():
    def __init__(self) -> None:
        self.home_lat = os.environ.get("home_lat")
        self.home_long = os.environ.get("home_long")
        self.APP_ID = os.environ.get("APP_ID")
        self.APP_KEY_WU = os.environ.get("APP_KEY_WU")
        self.APP_KEY_OW = os.environ.get("APP_KEY_OW")
        self.url_WU = f"http://api.weatherunlocked.com/api/current/{self.home_lat},{self.home_long}?app_id={self.APP_ID}&app_key={self.APP_KEY_WU}"
        self.url_OW = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.home_lat}&lon={self.home_long}&appid={self.APP_KEY_OW}&units=metric"

    def get_response_WU(self):
        with requests.Session() as req:
            response_WU = req.get(self.url_WU)
            return response_WU

    def get_response_OW(self):
        with requests.Session() as req:
            response_OW = req.get(self.url_OW)
            return response_OW

    def create_dict_OW(self, response_OW, time):
        data = response_OW.json()
        data_dict = {}
        data_dict["time"] = time
        data_dict["lat"] = self.home_lat
        data_dict["long"] = self.home_long
        data_dict["wx_desc"] = data["list"][0]["weather"][0]["description"]
        data_dict["feelslike_c"] = data["list"][0]["main"]["feels_like"]
        data_dict["temp_c"] = data["list"][0]["main"]["temp"]
        return data_dict
        
    def check_response(self, response):
        return response.ok
    
    def get_time(self):
        time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        '''datatype is string'''
        return time

    def create_dict_WU(self, response, time):
        response_dict = json.loads(response.text)
        data_dict = {}
        data_dict["time"] = time
        data_dict["lat"] = self.home_lat
        data_dict["long"] = self.home_long
        data_dict["wx_desc"] = response_dict["wx_desc"]
        data_dict["feelslike_c"] = response_dict["feelslike_c"]
        data_dict["temp_c"] = response_dict["temp_c"]
        return data_dict



if __name__ == "__main__":
    my_weather_api = WeatherApi()
    response = my_weather_api.get_response_WU()
    time = my_weather_api.get_time()
    if my_weather_api.check_response(response):
        dict = my_weather_api.create_dict(response=response, time=time)
        print(dict)
    elif not my_weather_api.check_response(response):
        response = my_weather_api.get_response_OW()
        time = my_weather_api.get_time()
        dict = my_weather_api.create_dict_OW(response_OW=response, time=time)
        print(dict)
    
