from flask import Blueprint, jsonify, request
from pulse.integration.fmpapi_to_db import FmpApiToDatabase


pulse_load = Blueprint("pulse_load", __name__)

@pulse_load.route('/load_index_companies', methods=['GET'])
def get_index_companies():
    FmpApiToDatabase.load_index_companies()
    message = "loaded index companies successfully"
    return message


