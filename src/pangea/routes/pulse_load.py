from flask import Blueprint, jsonify, request
from pulse.integration.fmpapi_to_db import FmpApiToDatabase

pulse_load = Blueprint('pulse_load',__name__)

query_string_to_function_mapping = {
        "indexCompanies":{
            "api_name":FmpApiToDatabase.load_index_companies,
            "message": "Loaded index companies data successfully"
        }, 
        "globalStocks":{
            "api_name":FmpApiToDatabase.load_global_stocks,
            "message": "Loaded global stocks data successfully"
        }, 
        "historicalPrices":{
            "api_name":FmpApiToDatabase.load_historical_prices,
            "message": "Loaded historical prices data successfully"
        }, 
        "dailyPrices":{
            "api_name":FmpApiToDatabase.load_daily_prices,
            "message": "Loaded daily prices data successfully"
        }, 
        "compEstimates":{
            "api_name":FmpApiToDatabase.load_comp_estimates,
            "message": "Loaded company estimates data successfully"
        }, 
        "compRatings":{
            "api_name":FmpApiToDatabase.load_comp_ratings,
            "message": "Loaded company ratings data successfully"
        }, 
        "compRecom":{
            "api_name":FmpApiToDatabase.load_comp_recom,
            "message": "Loaded company recommendations data successfully"
        } 
    }   

@pulse_load.route('/pulse/load', methods=['GET'])
def get_load_pulse_data():
    # Reading query parameter 'data' from request
    selected_data= request.args.get('data')    
    function_mapping = query_string_to_function_mapping.get(selected_data)
    try:
        if function_mapping:
            function_mapping.get("api_name")()
            response = jsonify({"message": function_mapping.get("message")}),200
        else:
            response=jsonify({"error": "Bad Request ---Invalid data"}),400           
    except Exception as e:
        response = jsonify({"error": "Internal Server Error","Exception": str(e)}),500
    return response


