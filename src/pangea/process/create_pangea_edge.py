import requests
import json

endpoints = ['/sectors/marketcap', '/sectors', '/sectors/periodic_marketcap_data']

class PangeaEdge:

    def __init__(self, base_url) :
        self.base_url = base_url

    def get_api_url(self, endpoint):
        return self.base_url + endpoint

    # Function to fetch data from an API endpoint
    def fetch_data(self, endpoint):
        try:
            response = requests.get(self.get_api_url(endpoint))
            data = response.json()
            print(f"Data fetching from API endpoint {endpoint} is Done")
            return data
        except Exception as error:
            print(f"Error fetching data from {endpoint}: {error}")
            raise error

    # Function to combine and save data to a file
    def createEdge(self):
        try:
            edge_data = {}
            for endpoint in endpoints:
                edge_data[endpoint] = self.fetch_data(endpoint)

            minified_edge_data = json.dumps(edge_data, separators=(',', ':'))

            # Save combined data to a file
            fileName = 'pangea_edge.json'
            with open(fileName, 'w') as file:
                file.write(minified_edge_data)

            print(f"Pangea Edge data saved to {fileName}")
        except Exception as error:
            print(f"Error saving Pangea Edge data: {error}")

    # Call the function to combine and save data
    
pangea = PangeaEdge("http://localhost:5000/")
pangea.createEdge()

