from core.configuration.config import Config
from pulse.fmpapi.get_api import GetApi
import datetime

import requests


class Global_stocks(GetApi):
    def __init__(self)->None:
        super().__init__("stock/list?")

class Historical_prices(GetApi):
    
    def __init__(self, symbol)->None :
        current_date = datetime.date.today()
<<<<<<< Updated upstream:src/pulse/fmpapi/stock_prices.py
        date_str = current_date.strftime('%Y-%m-%d')
        self.api_config = GetApi.config.load_config()['FmpApi']
        query = "historical-price-full/" + symbol + "?from=" + self.api_config['from_date'] + "&to=" + date_str + "&"
=======
        date = current_date.strftime('%Y-%m-%d')
        self.api_config = GetApi.config.load_config()['FmpApi']
        query = f"historical-price-full/{symbol}?from={self.api_config['from_date']}&to={date}&"
>>>>>>> Stashed changes:src/pulse/fmpapi/stock_prices_api.py
        super().__init__(query)
    
class Historical_market_cap(GetApi):
    def __init__(self, symbol)->None:
        query = "historical-market-capitalization/" + symbol + "?limit=2000&"
        super().__init__(query)

class Daily_prices(GetApi):
    def __init__(self, symbol)->None :
        query = "quote/" + symbol +"?"
        super().__init__(query)