from flask import Blueprint, jsonify, request
from pulse.integration.fmpapi_to_db import FmpApiToDatabase
from pangea.process.create_pangea_edge import PangeaEdge

pangea_edge = Blueprint("pangea_edge", __name__)


@pangea_edge.route("/pangea/edge", methods=["GET"])
def get_edge_data():
    try:
        base_url = request.host_url
        pe = PangeaEdge(base_url)
        pe.createEdge()
        response = jsonify({"message": f"Pangea Edge is created successfully"}), 200
    except Exception as e:
        response = jsonify({"error": "Internal Server Error", "Exception": str(e)}), 500
    return response
