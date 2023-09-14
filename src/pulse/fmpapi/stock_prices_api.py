from pulse.fmpapi.get_api import GetApi
import datetime


class Global_stocks(GetApi):
# The class just need to fill in the details of the query string for global stocks. 
# The Base class takes care of all the execution of the rest of the functionality.
    def __init__(self)->None:
        super().__init__("stock/list?")


class Historical_prices(GetApi):
# The class just need to fill in the details of the query string for historical price 
# data. The Base class takes care of all the execution of the rest of the functionality.
    def __init__(self, symbol)->None :
        current_date = datetime.date.today()
        date = current_date.strftime('%Y-%m-%d')
        self.api_config = GetApi.config.load_config()["FmpApi"]
        query = f"historical-price-full/{symbol}?from={self.api_config['from_date']}&to={date}&"
        super().__init__(query)
    
class Historical_market_cap(GetApi):
# The class just need to fill in the details of the query string for historical marketcap 
# data. The Base class takes care of all the execution of the rest of the functionality.
    def __init__(self, symbol)->None:
        query = "historical-market-capitalization/" + symbol + "?limit=2000&"
        super().__init__(query)

class Daily_prices(GetApi):
# The class just need to fill in the details of the query string for particular day price 
# data. The Base class takes care of all the execution of the rest of the functionality.
    def __init__(self, symbol)->None :
        query = "quote/" + symbol +"?"
        super().__init__(query)