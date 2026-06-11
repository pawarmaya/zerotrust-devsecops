import requests

SONAR_URL = "http://localhost:9000"
TOKEN = "squ_8b3f0bb2fcfcc69275faedba7a214db5dd390785"

response = requests.get(
    f"{SONAR_URL}/api/system/status",
    auth=(TOKEN, "")
)

print(response.json())
