from pulse.repository.database_connect import DatabaseConnect
from pulse.repository.index_companies_repo import SP500_table
from pulse.repository.stock_prices_repo import Daily_prices_table
from pulse.repository.stock_prices_repo import Historical_prices_table
from sqlalchemy import func
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
# This class has all the different queries of different tables that can be used.
class Queries:
    def get_sectors(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            # Query the database for sectors
            sectors = session.query(SP500_table.sector).distinct().all()
            # Convert the data to a list of dictionaries
            data = [{"sector": sector} for sector, in sectors]
            return data
        
    def get_sectors_subsectors(self, selected_sector=None):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            if selected_sector:
                # Query the database for subsectors based on the selected sector
                sectors_and_subsectors = session.query(SP500_table.sector, SP500_table.subsector).filter(SP500_table.sector == selected_sector).distinct().all()
            else:
                # Query all subsectors
                sectors_and_subsectors = session.query(SP500_table.sector, SP500_table.subsector).distinct().all()
        # Convert the data to a list of dictionaries
        data = [{"sector": sector, "subSector": subsector} for sector, subsector in sectors_and_subsectors]
        return data
        
    def get_symbols(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            symbols_query = session.query(SP500_table.symbol).all()
            symbols = [symbol[0] for symbol in symbols_query]
            return symbols
        
    def get_sector_marketcap(self, selected_sector=None):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
        # Query the SP500_table to get all symbols in the selected sector
            sector_companies = session.query(SP500_table.symbol).filter(SP500_table.sector == selected_sector).all()
            symbols = [company[0] for company in sector_companies]

            # Calculate the total market cap for companies in the selected sector
            total_marketcap = (
                session.query(func.sum(Daily_prices_table.market_cap))
                .filter(Daily_prices_table.symbol.in_(symbols))
                .scalar()
            )
            formatted_market_cap = f"${total_marketcap:,}"

        return {"sector": selected_sector, "total_marketcap": formatted_market_cap}
    


    def get_all_sectors_marketcap(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        
        with session() as session:
            # Query all sectors in SP500
            sectors = session.query(SP500_table.sector).distinct().all()
            sectors = [sector[0] for sector in sectors]

            sector_marketcaps = {}
            
            for sector in sectors:
                # Query the SP500_table to get all symbols in the current sector
                sector_companies = session.query(SP500_table.symbol).filter(SP500_table.sector == sector).all()
                symbols = [company[0] for company in sector_companies]

                # Calculate the total market cap for companies in the current sector
                total_marketcap = (
                    session.query(func.sum(Daily_prices_table.market_cap))
                    .filter(Daily_prices_table.symbol.in_(symbols))
                    .scalar()
                )

                # Format the market cap for the current sector
                formatted_market_cap = f"${total_marketcap:,}"
                
                # Store the market cap for the sector in the dictionary
                sector_marketcaps[sector] = formatted_market_cap
        
        return sector_marketcaps
    
    def get_previous_working_date(previous_date):
        date = previous_date
        if date.weekday() == 5:  # Saturday
            previous_working_day = date - timedelta(days=1)
        elif date.weekday() == 6:  # Sunday
            previous_working_day = date - timedelta(days=2)
        else:
            previous_working_day = date

        return previous_working_day
    
    def get_periodic_marketcap_for_sectors(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()

        # Get today's date as a datetime object
        today = date.today()
        today = today - timedelta(days=1)

        # Calculate the previous date by subtracting one day
        previous_date = today - timedelta(days=1)
        previous_working_date = Queries.get_previous_working_date(previous_date)

        # Calculate the one week back date by subtracting 7 days
        oneweek_back_Date = today - timedelta(days=7)
        oneweek_back_working_date = Queries.get_previous_working_date(oneweek_back_Date)

        # Calculate the date one month back
        one_month_back = today - relativedelta(months=1)   
        one_month_back_working_date = Queries.get_previous_working_date(one_month_back)

        # Calculate the date three months back
        three_months_back = today - relativedelta(months=3)
        three_months_back_working_date = Queries.get_previous_working_date(three_months_back)

        # Calculate the date six months back
        six_months_back = today - relativedelta(months=6)
        six_months_back_working_date = Queries.get_previous_working_date(six_months_back)

        # Calculate the date one year back, considering leap years
        one_year_back = today - relativedelta(years=1)
        one_year_back_working_date = Queries.get_previous_working_date(one_year_back)


        with session() as session:
            # Query all sectors in SP500
            sectors = session.query(SP500_table.sector).distinct().all()
            sectors = [sector[0] for sector in sectors]

            periodic_marketcap_for_sectors = {}
            sector_periodic_marketcap_data = []
            for sector in sectors:
                # Query the SP500_table to get all symbols in the current sector
                sector_companies = session.query(SP500_table.symbol).filter(SP500_table.sector == sector).all()
                symbols = [company[0] for company in sector_companies]

                # Calculate the total market cap for companies in the current sector
                current_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(Historical_prices_table.symbol.in_(symbols), func.date(Historical_prices_table.date_time) == today)
                    .scalar()
                )

                previous_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(Historical_prices_table.symbol.in_(symbols), func.date(Historical_prices_table.date_time) == previous_working_date)
                    .scalar()
                )
                
                oneweek_back_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(Historical_prices_table.symbol.in_(symbols), func.date(Historical_prices_table.date_time) == oneweek_back_working_date)
                    .scalar()
                )

                onemonth_back_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(Historical_prices_table.symbol.in_(symbols), func.date(Historical_prices_table.date_time) == one_month_back_working_date)
                    .scalar()
                )

                threemonth_back_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(Historical_prices_table.symbol.in_(symbols), func.date(Historical_prices_table.date_time) == three_months_back_working_date)
                    .scalar()
                )

                sixmonth_back_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(Historical_prices_table.symbol.in_(symbols), func.date(Historical_prices_table.date_time) == six_months_back_working_date)
                    .scalar()
                )

                oneyear_back_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(Historical_prices_table.symbol.in_(symbols), func.date(Historical_prices_table.date_time) == one_year_back_working_date)
                    .scalar()
                )

                # Format the current market cap for the current sector
                formatted_current_market_cap = current_marketcap

                # Format the previous market cap for the current sector
                formatted_previous_market_cap = previous_marketcap

                # Format the one week back market cap for the current sector
                formatted_oneweek_back_market_cap = oneweek_back_marketcap

                # Format the one month back market cap for the current sector
                formatted_onemonth_back_market_cap = onemonth_back_marketcap

                # Format the three month back market cap for the current sector
                formatted_threemonth_back_market_cap = threemonth_back_marketcap

                # Format the six month back market cap for the current sector
                formatted_sixmonth_back_market_cap = sixmonth_back_marketcap

                # Format the one year back market cap for the current sector
                formatted_oneyear_back_market_cap = oneyear_back_marketcap


                sector_periodic_marketcap_data.append((sector, formatted_current_market_cap, formatted_previous_market_cap, formatted_oneweek_back_market_cap, formatted_onemonth_back_market_cap, formatted_threemonth_back_market_cap, formatted_sixmonth_back_market_cap, formatted_oneyear_back_market_cap))

                
                # Store the market cap for the sector in the dictionary
                #periodic_marketcap_for_sectors[sector] = formatted_market_cap

            periodic_marketcap_for_sectors = [{"sector": sector, "current_marketcap": formatted_current_market_cap, "previous_marketcap": formatted_previous_market_cap, "oneweek_back": formatted_oneweek_back_market_cap, "onemonth_back": formatted_onemonth_back_market_cap, "threemonths_back": formatted_threemonth_back_market_cap, "sixmonths_back": formatted_sixmonth_back_market_cap, "oneyear_back": formatted_oneyear_back_market_cap} for sector, formatted_current_market_cap, formatted_previous_market_cap, formatted_oneweek_back_market_cap, formatted_onemonth_back_market_cap, formatted_threemonth_back_market_cap, formatted_sixmonth_back_market_cap, formatted_oneyear_back_market_cap in sector_periodic_marketcap_data]

        return periodic_marketcap_for_sectors