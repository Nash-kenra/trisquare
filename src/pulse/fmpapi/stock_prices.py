from core.configuration.config import Config
from pulse.fmpapi.get_api import GetApi

import requests


class Global_stocks(GetApi):
    def __init__(self)->None:
        super().__init__("stock/list?")

class Historical_prices(GetApi):
    def __init__(self, symbol,date)->None :

        query = "historical-price-full/" + symbol + "?from=2017-01-01&to=" + date + "&"
        super().__init__(query)
    
class Historical_market_cap(GetApi):
    def __init__(self, symbol)->None:
        query = "historical-market-capitalization/" + symbol + "?limit=2000&"
        super().__init__(query)

class Daily_prices(GetApi):
    def __init__(self, symbol)->None :
        query = "quote/" + symbol +"?"
        super().__init__(query)