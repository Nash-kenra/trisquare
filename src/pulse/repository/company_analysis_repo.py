from sqlalchemy import Column, String, DateTime, Float,INTEGER
from sqlalchemy.orm import declarative_base
from pulse.repository.pulsedb_base import PulseDB_Base


Base = declarative_base()


class Comp_Estimates_table(Base, PulseDB_Base):
# Entity class for the DB table Global companies. 

# Manage all the operations like loading the data from the comp_estimates table.


    __tablename__ = 'comp_estimates'
    symbol = Column(String, primary_key=True)
    date_time = Column(DateTime, primary_key=True)
    estimatedrevenuelow = Column(Float)
    estimatedrevenuehigh = Column(Float)
    estimatedrevenueavg = Column(Float)
    estimatedebitdalow = Column(Float)
    estimatedebitdahigh = Column(Float)
    estimatedebitdaavg = Column(Float)
    estimatedebitlow = Column(Float)
    estimatedebithigh = Column(Float)
    estimatedebitavg = Column(Float)
    estimatednetincomelow = Column(Float)
    estimatednetincomehigh = Column(Float)
    estimatednetincomeavg = Column(Float)
    estimatedsgaexpenselow = Column(Float)
    estimatedsgaexpensehigh = Column(Float)
    estimatedsgaexpenseavg = Column(Float)
    estimatedepsavg = Column(Float)
    estimatedepshigh = Column(Float)
    estimatedepslow = Column(Float)
    numberanalystestimatedrevenue = Column(INTEGER)
    numberanalystsestimatedeps = Column(INTEGER)

    


    def getBase(self):
        return Base

    def convert(self, element):
        row = Comp_Estimates_table(
            symbol=element["symbol"],
            date_time=element["date"],
	        estimatedrevenuelow=element["estimatedRevenueLow"],
            estimatedrevenuehigh=element["estimatedRevenueHigh"],
            estimatedrevenueavg=element["estimatedRevenueAvg"],
            estimatedebitdalow=element["estimatedEbitdaLow"],
            estimatedebitdahigh=element["estimatedEbitdaHigh"],
            estimatedebitdaavg=element["estimatedEbitdaAvg"],
            estimatedebitlow=element["estimatedEbitLow"],
            estimatedebithigh=element["estimatedEbitHigh"],
            estimatedebitavg=element["estimatedEbitAvg"],
            estimatednetincomelow=element["estimatedNetIncomeLow"],
            estimatednetincomehigh=element["estimatedNetIncomeHigh"],
            estimatednetincomeavg=element["estimatedNetIncomeAvg"],
            estimatedsgaexpenselow=element["estimatedSgaExpenseLow"],
            estimatedsgaexpensehigh=element["estimatedSgaExpenseHigh"],
            estimatedsgaexpenseavg=element["estimatedSgaExpenseAvg"],
            estimatedepsavg=element["estimatedEpsAvg"],
            estimatedepshigh=element["estimatedEpsHigh"],
            estimatedepslow=element["estimatedEpsLow"],
            numberanalystestimatedrevenue=element["numberAnalystEstimatedRevenue"],
            numberanalystsestimatedeps=element["numberAnalystsEstimatedEps"] 
        )
        return row

