from flask import Blueprint, jsonify, request
from pulse.repository.queries import Queries

sectors = Blueprint("sectors", __name__)

@sectors.route('/sectors', methods=['GET'])
def get_sectors():
    query = Queries()
    return jsonify(query.get_sectors())

@sectors.route('/sectors/subsectors', methods=['GET'])
def get_sectors_subsectors():
    query = Queries()
    selected_sector = request.args.get('sector')  
    subsectors = query.get_sectors_subsectors(selected_sector)
    return jsonify(subsectors)


@sectors.route('/sectors/<string:selected_sector>/marketcap', methods=['GET'])
def get_sector_marketcap(selected_sector):
    query = Queries()
    data = query.get_sector_marketcap(selected_sector)
    return jsonify(data)
    
