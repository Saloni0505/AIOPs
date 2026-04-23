import requests

response = requests.post("http://localhost:5001/reset")
print(response.json())