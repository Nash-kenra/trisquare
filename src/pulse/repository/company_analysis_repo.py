from sqlalchemy import Column, String, DateTime, Float,INTEGER
from sqlalchemy.orm import declarative_base
from pulse.repository.pulsedb_base import PulseDB_Base


Base = declarative_base()


class Comp_estimates_table(Base, PulseDB_Base):
# Entity class for the DB table comp_estimates. 

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
        row = Comp_estimates_table(
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

class Comp_ratings_table(Base, PulseDB_Base):
# Entity class for the DB table Comp_ratings. 
# Manage all the operations like loading the data from the Comp_ratings table.

    __tablename__ = 'comp_ratings'
    symbol = Column(String, primary_key=True)
    date_time = Column(DateTime, primary_key=True)
    rating = Column(String)
    rating_score = Column(INTEGER)
    rating_recommendation = Column(String)
    rating_details_dcf_score = Column(INTEGER)
    rating_details_dcf_recommendation = Column(String)
    rating_details_roe_score = Column(INTEGER)
    rating_details_roe_recommendation = Column(String)
    rating_details_roa_score = Column(INTEGER)
    rating_details_roa_recommendation = Column(String)
    rating_details_de_score = Column(INTEGER)
    rating_details_de_recommendation = Column(String)
    rating_details_pe_score = Column(INTEGER)
    rating_details_pe_recommendation = Column(String)
    rating_details_pb_score = Column(INTEGER)
    rating_details_pb_recommendation = Column(String)

    def getBase(self):
        return Base

    def convert(self, element):
        row = Comp_ratings_table(
                symbol=element["symbol"],
                date_time=element["date"],
                rating=element["rating"],
                rating_score=element["ratingScore"],
                rating_recommendation=element["ratingRecommendation"],
                rating_details_dcf_score=element["ratingDetailsDCFScore"],
                rating_details_dcf_recommendation=element["ratingDetailsDCFRecommendation"],
                rating_details_roe_score=element["ratingDetailsROEScore"],
                rating_details_roe_recommendation=element["ratingDetailsROERecommendation"],
                rating_details_roa_score=element["ratingDetailsROAScore"],
                rating_details_roa_recommendation=element["ratingDetailsROARecommendation"],
                rating_details_de_score=element["ratingDetailsDEScore"],
                rating_details_de_recommendation=element["ratingDetailsDERecommendation"],
                rating_details_pe_score=element["ratingDetailsPEScore"],
                rating_details_pe_recommendation=element["ratingDetailsPERecommendation"],
                rating_details_pb_score=element["ratingDetailsPBScore"],
                rating_details_pb_recommendation=element["ratingDetailsPBRecommendation"]
        )
        return row

class Comp_recom_table(Base, PulseDB_Base):
    # Entity class for the DB table comp_recom.       
    __tablename__='comp_recom' 
    symbol = Column(String, primary_key=True)
    date_time = Column(DateTime, primary_key=True)
    analyst_ratings_buy = Column(INTEGER)
    analyst_ratings_hold = Column(INTEGER)
    analyst_ratings_sell  = Column(INTEGER)
    analyst_ratings_strong_sell= Column(INTEGER)
    analyst_ratings_strong_buy= Column(INTEGER)
    
    def getBase(self):
        return Base
    # Mapping response elements to table colums.
    def convert(self, element):
        row = Comp_recom_table(
                symbol=element["symbol"],
                date_time=element["date"],
                analyst_ratings_buy=element["analystRatingsbuy"],
                analyst_ratings_hold=element["analystRatingsHold"],
                analyst_ratings_sell=element["analystRatingsSell"],
                analyst_ratings_strong_sell=element["analystRatingsStrongSell"],
                analyst_ratings_strong_buy=element["analystRatingsStrongBuy"]
        )
        return row    

