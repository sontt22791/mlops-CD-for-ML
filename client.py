import requests
import json

url = "http://localhost:5000/predict"

input_data = '["MLOps is critical for robustness"]'

# Set the content type
headers = {"Content-Type": "application/json"}

# Make the request and display the response
resp = requests.post(url, input_data, headers=headers)
print(resp.json())