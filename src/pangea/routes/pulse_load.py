from flask import Blueprint, jsonify, request
from pulse.integration.fmpapi_to_db import FmpApiToDatabase


pulse_load = Blueprint("pulse_load", __name__)

# @pulse_load.route('/load_index_companies', methods=['GET'])
# def get_index_companies():
#     FmpApiToDatabase.load_index_companies()
#     message = "loaded index companies successfully"
#     return message

@pulse_load.route('/pulse/load', methods=['GET'])
def get_load_pulse_data():
    selected_data = request.args.get('data')  
    try:
        if selected_data=="indexCompanies":
            FmpApiToDatabase.load_index_companies() 
            message = "loaded index companies successfully"
        elif selected_data=="globalStocks":
            FmpApiToDatabase.load_global_stocks()
            message = "loaded global stocks successfully"
        elif selected_data=="historicalPrices":
            FmpApiToDatabase.load_historical_prices()
            message = "loaded historical prices successfully"
        elif selected_data=="dailyPrices":
            FmpApiToDatabase.load_daily_prices()
            message = "loaded daily prices successfully"
        elif selected_data=="compEstimates":
            FmpApiToDatabase.load_comp_estimates()
            message = "loaded company estimates successfully"
        elif selected_data=="compRatings":
            FmpApiToDatabase.load_comp_ratings()
            message = "loaded comapany ratings successfully"
        elif selected_data=="compRecom":
            FmpApiToDatabase.load_comp_recom()
            message = "loaded company recommendations successfully"
        else:
            response = jsonify({"Error": "Bad Request - Inavlid data"})
            response.status_code = 400 
            return response
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "exception": str(e)}), 500

    return jsonify({"Message":message}), 200


