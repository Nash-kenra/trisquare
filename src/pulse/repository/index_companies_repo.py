from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
from pulse.repository.pulsedb_base import PulseDB_Base

Base = declarative_base()


class SP500_table(Base, PulseDB_Base):
# Entity class for the DB table SP500 companies. 
# Manage all the operations like loading the data from the SP500 table.
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


class Nasdaq_table(Base,PulseDB_Base):
# Entity class for the DB table NASDAQ companies. 
# Manage all the operations like loading the data from the NASDAQ table.

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
        row = Nasdaq_table(
            symbol=element["symbol"],
            company_name=element["name"],
            sector=element["sector"],
            subsector=element["subSector"],
            headquarter=element["headQuarter"],
            cik=element["cik"],
            founded=element["founded"]
        )
        return row

class Dowjones_table(Base, PulseDB_Base):
# Entity class for the DB table DOWJONES companies. 
# Manage all the operations like loading the data from the DOWJONES table.

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
        row = Dowjones_table(
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
    
