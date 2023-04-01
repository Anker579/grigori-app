import requests
import datetime as dt
import json
from dotenv import dotenv_values
config = dotenv_values(".env")



class WeatherApi():
    def __init__(self) -> None:
        self.home_lat = config["home_lat"]
        self.home_long = config["home_long"]
        self.APP_ID = config["APP_ID"]
        self.APP_KEY = config["APP_KEY"]
        self.url = f"http://api.weatherunlocked.com/api/current/{self.home_lat},{self.home_long}?app_id={self.APP_ID}&app_key={self.APP_KEY}"

    def get_response(self):
        with requests.Session() as req:
            response = req.get(self.url)
            return response
        
    def check_response(self, response):
        return response.ok
    
    def get_time(self):
        time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        '''datatype is string'''
        return time

    def create_dict(self, response, time):
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
    response = my_weather_api.get_response()
    time = my_weather_api.get_time()
    if my_weather_api.check_response(response):
        dict = my_weather_api.create_dict(response=response, time=time)
        print(dict)
