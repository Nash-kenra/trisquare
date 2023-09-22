from core.configuration.config import Config
import requests
import datetime
import time


class GetApi:
    # Access Financial Modeling Prep APIs
    # It constructs the query string depending on the API and fetches the data
    # The data will be retured from the API is in the JSON format
    # The class is the base class for all the APIs. It does all the functionality of building the URL
    # and fetches the data.
    # All the sub classes just needs to provide the query string depending on the API.

    config = Config()

    # As per our subscription, we can make only 300 calls per minute. So if we exceed 300, then API doesn't respond. 
    # It's causing an error especially loading historical data for all the stocks. 
    # The below parameters are required for throttling the requests to FMP API

    # These are all class level variables to control the number of calls. Typically GetApi is instantiated for each API call
    # But we need to have a counter on number of calls made to API. So you need class variables to take care of this situation
    # We will be counting the number of calls across the app, and if it exceeds the limit, we will be sleeping for the rest of the time
    # and resume it, so we will not be missing tje calls.  
    #     
    TOTAL_CALLS_PER_MINUTE = 280
    MINUTE = 60
    completed_calls = 0
    timer = 0
    timer_start_time = datetime.datetime.now()

    def __init__(self, query_string) -> None:
        self.api_config = GetApi.config.load_config()["FmpApi"]
        self.api_response = None
        self.query_string = query_string

    def get_uri(self):
        return self.api_config["uri"]

    def get_api_key(self):
        return self.api_config["key"]

    def get_url(self):
        return self.get_uri() + self.query_string + self.get_api_key()

    def api_call(self):
        url = self.get_url()
        response = requests.get(url)
        jsondata = response.json()
        return jsondata

    def fetch(self):
        return self.throttle(self.api_call)

    # Throttling the calls across the app
    def throttle(self, api):
        
        if GetApi.completed_calls > GetApi.TOTAL_CALLS_PER_MINUTE and GetApi.timer < GetApi.MINUTE:
            
            print(f"Total calls made so far : {GetApi.completed_calls}")
            sleep_time = GetApi.MINUTE - GetApi.timer
            print(f"Sleep time for : {sleep_time}")
            time.sleep(sleep_time)
            GetApi.completed_calls = 0
            
        api_begin_time = datetime.datetime.now()
        response = api()
        api_end_time = datetime.datetime.now()
        if GetApi.completed_calls == 0:
            GetApi.timer_start_time = api_begin_time

        GetApi.completed_calls = GetApi.completed_calls + 1
        
        time_diff = api_begin_time - GetApi.timer_start_time 
        GetApi.timer = int(time_diff.total_seconds())

        return response
        