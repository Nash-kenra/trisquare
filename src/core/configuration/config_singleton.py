import json

class config_singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(config_singleton, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance
    
    def load_config(self):
        
        try:
            with open('./core/configuration/config.json', 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print(f"Configuration file 'config.json' not found.")
            self.config = {}

        return self.config
    

