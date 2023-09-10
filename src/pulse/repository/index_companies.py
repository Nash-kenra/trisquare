from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
from pulse.repository.database_connect import DatabaseConnect
from pulse.repository.pulsedb_base import PulseDB_Base

Base = declarative_base()


class SP500_table(Base, PulseDB_Base):
# Entity class for the DB table SP500 companies. 
# Manage all the operations like loading and fetching the data from the SP500 table.
    __tablename__ = 'sp500'
    symbol = Column(String, primary_key=True)
    company_name = Column(String)
    sector = Column(String)
    subsector = Column(String)
    headquarter = Column(String)
    datefirstadded = Column(String)
    cik = Column(String)
    founded = Column(String)
    base = Base

    def getBase(self):
        return Base

    def convert(self, element):
        row = SP500_table(
                symbol=element["symbol"],
                company_name=element["name"],
                sector=element["sector"],
                subsector=element["subSector"],
                headquarter=element["headQuarter"],
                datefirstadded=element["dateFirstAdded"],
                cik=element["cik"],
                founded=element["founded"]
            )
        return row
      
    def get_sectors(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            # Query the database for sectors
            sectors = session.query(SP500_table.sector).distinct().all()
            # Convert the data to a list of dictionaries
            data = [{"sector": sector} for sector, in sectors]
            return data
        
    def get_sectors_subsectors(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            sectors_and_subsectors = session.query(SP500_table.sector, SP500_table.subSector).distinct().all()
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


class NASDAQ_table(Base,PulseDB_Base):
# Entity class for the DB table NASDAQ companies. 
# Manage all the operations like loading and fetching the data from the NASDAQ table.

    __tablename__ = 'nasdaq'
    symbol = Column(String, primary_key=True)
    company_name = Column(String)
    sector = Column(String)
    subsector = Column(String)
    headquarter = Column(String)
    cik = Column(String)
    founded = Column(DateTime)
    
    def getBase(self):
        return Base
    
    def convert(self, element):
        row = NASDAQ_table(
            symbol=element["symbol"],
            company_name=element["name"],
            sector=element["sector"],
            subsector=element["subSector"],
            headquarter=element["headQuarter"],
            cik=element["cik"],
            founded=element["founded"]
        )
        return row

class DOWJONES_table(Base, PulseDB_Base):
# Entity class for the DB table DOWJONES companies. 
# Manage all the operations like loading and fetching the data from the DOWJONES table.

    __tablename__ = 'dowjones'
    symbol = Column(String, primary_key=True)
    company_name = Column(String)
    sector = Column(String)
    subsector = Column(String)
    headquarter = Column(String)
    datefirstadded = Column(DateTime)
    cik = Column(String)
    founded = Column(DateTime)

    def getBase(self):
        return Base

    def convert(self, element):
        row = DOWJONES_table(
            symbol=element["symbol"],
            company_name=element["name"],
            sector=element["sector"],
            subsector=element["subSector"],
            headquarter=element["headQuarter"],
            datefirstadded=element["dateFirstAdded"],
            cik=element["cik"],
            founded=element["founded"]
        )
        return row
    
