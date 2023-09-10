import json
class Config:
# It has all the Configuration settings needed for the application
# The settings typically contain
# 1. DB connection details 
# 2. API Url, keys, query strings
# ToDo:
# The class needs to be designed and implemented as a singleton as it's very critical to load the
# setting only once. 

    def __init__(self) -> None:
        self.settings = None
        
    def load_config(self):
        with open('./core/configuration/config.json') as f:
            settings = json.load(f)
            return settings
            