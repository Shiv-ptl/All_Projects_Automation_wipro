#from http.client import responses
# https://videogamedb.uk:443/api/v2/videogame
from requests.auth import HTTPBasicAuth

import  requests

try:
    headers = {
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    }
    #make a get request to a api endpoint
    response = requests.get("https://videogamedb.uk:443/api/v2/videogame",auth=HTTPBasicAuth('username', 'password'),timeout= 5,headers= headers)
    print(response)

    #check if type status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 k")
        #parse the json file
        data = response.json()
        print(data)

    else:print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred : {e}")