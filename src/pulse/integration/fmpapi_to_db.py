from pulse.fmpapi.get_api import SP500
from pulse.fmpapi.get_api import Nasdaq
from pulse.fmpapi.get_api import Dowjones
from pulse.fmpapi.get_api import Stockprices
from pulse.fmpapi.get_api import Historicprices
from pulse.fmpapi.get_api import Global_stocks
from pulse.fmpapi.get_api import Global_etfs
from pulse.repository.index_companies import SP500_table
from pulse.repository.index_companies import NASDAQ_table
from pulse.repository.index_companies import DOWJONES_table
from pulse.repository.stock_prices import Global_stocks_table
from pulse.repository.stock_prices import Global_etfs_table
from pulse.repository.stock_prices import Stock_prices_table
from pulse.repository.stock_prices import Historic_prices_table
from pulse.combine.combine import Combine

class FmpApiToDatabase():
# Controller calls the FMPAPI and gets the JSON data. 
# This data is passed to the tables for loading. 
# Mainly focus on loading all the index companies from SP500, NASDAQ and DOWJONES

    def load_SP500_companies():

        sp500_api = SP500()
        sp500_json_data = sp500_api.fetch()
        print("Fetched sp500 json data from API")

        sp500_repo = SP500_table()
        # sp500.create_table(sp500_repo.getBase())
        sp500_repo.load_data(sp500_json_data)
        print("loaded sp500 API data into sp500 table")

    def load_Nasdaq_companies():

        nasdaq_api = Nasdaq()
        nasdaq_json_data = nasdaq_api.fetch()
        print("Fetched Nasdaq json data from API")

        nasdaq_repo = NASDAQ_table()
        # nasdaq_repo.create_table(nasdaq_repo.getBase())
        nasdaq_repo.load_data(nasdaq_json_data)
        print("loaded Nasdaq API data into Nasdaq table")

    def load_Dowjones_companies():
        dowjones_api = Dowjones()
        dowjones_json_data = dowjones_api.fetch()
        print("Fetched Dowjones json data from API")

        dowjones_repo = DOWJONES_table()
        # dowjones_repo.create_table(dowjones_repo.getBase())
        dowjones_repo.load_data(dowjones_json_data)
        print("loaded Dowjones API data into Dowjones table")

    def load_global_stocks():
        global_stocks_api = Global_stocks()
        global_stocks_json_data = global_stocks_api.fetch()
        print("Fetched global stocks json data from API")

        global_stocks_repo = Global_stocks_table()
        # globalstocks_repo.create_table(globalstocks_repo.getBase())
        global_stocks_repo.load_data(global_stocks_json_data)
        print("loaded Global stock API data into globalstocks table")

    def load_global_etfs():

        global_etfs_api = Global_etfs()
        global_etfs_json_data = global_etfs_api.fetch()
        print("Fetched global etf json data from API")

        global_etfs_repo = Global_etfs_table()
        #global_etfs_repo.create_table(global_etfs_repo.getBase())
        global_etfs_repo.load_data(global_etfs_json_data)
        print("loaded Global etf API data into global etf table")

 
    def load_index_companies():
        FmpApiToDatabase.load_SP500_companies()
        FmpApiToDatabase.load_Nasdaq_companies()
        FmpApiToDatabase.load_Dowjones_companies()

    
