from pulse.fmpapi.get_api import GetApi


class Comp_Estimates(GetApi):
# The class just need to fill in the details of the query string for particular day price 
# data. The Base class takes care of all the execution of the rest of the functionality.
    def __init__(self, symbol)->None :
        query = "analyst-estimates/" + symbol +"?"
        super().__init__(query)

        
class Comp_Ratings(GetApi):
# The class just need to fill in the details of the query string for particular day price 
# data. The Base class takes care of all the execution of the rest of the functionality.
    def __init__(self, symbol)->None :
        query = "rating/" + symbol +"?"
        super().__init__(query)


class comp_recom(GetApi):
# The class just need to fill in the details of the query string for particular company recommendations
# data. The Base class takes care of all the execution of the rest of the functionality.
    def __init__(self, symbol)->None:
        query = "analyst-stock-recommendations/" + symbol +"?"
        super().__init__(query)
