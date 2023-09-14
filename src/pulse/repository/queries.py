from pulse.repository.database_connect import DatabaseConnect
from pulse.repository.index_companies_repo import SP500_table
from pulse.repository.stock_prices_repo import Daily_prices_table
from sqlalchemy import func

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

        return {"sector": selected_sector, "total_marketcap": total_marketcap}