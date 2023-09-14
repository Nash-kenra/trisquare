from flask import Blueprint, jsonify, request
from pulse.repository.queries import Queries
# The sectors.py here is used to create the routes using FlaskAPI.
sectors = Blueprint("sectors", __name__)

# This route gets the method in Queries class with query of getting sectors in sp500 
# and shows in /sectors route.
@sectors.route('/sectors', methods=['GET'])
def get_sectors():
    query = Queries()
    return jsonify(query.get_sectors())

# This route gets the method in Queries class with query of getting subsectorssectors
#  for perticular sector in sp500 and shows in /sectors/subsectors route.
@sectors.route('/sectors/subsectors', methods=['GET'])
def get_sectors_subsectors():
    query = Queries()
    selected_sector = request.args.get('sector')  
    subsectors = query.get_sectors_subsectors(selected_sector)
    return jsonify(subsectors)

# This route gets the method in Queries class with query of getting marketcap
# for perticular sector in sp500 and shows in /sectors/<string:selected_sector>/marketcap.
@sectors.route('/sectors/<string:selected_sector>/marketcap', methods=['GET'])
def get_sector_marketcap(selected_sector):
    query = Queries()
    market_cap = query.get_sector_marketcap(selected_sector)
    return jsonify(market_cap)
    
