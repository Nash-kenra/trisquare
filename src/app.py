from flask import Flask
from flask_cors import CORS
from pangea.routes import sectors
# This is a main file for the api. We created the routes. They are handled here.
# Run this app.py to get acces for api routes in browser. http://127.0.0.1:5000/{routes}
app = Flask(__name__)
CORS(app)

app.register_blueprint(sectors.sectors)

if __name__ == "__main__":
    app.run(debug=True)
